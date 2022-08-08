from hashlib import new
from django.shortcuts import redirect, render
from django.views.generic.base import View
from django.contrib.sites.shortcuts import get_current_site
from .models import CustomUser
from .utils import EmailSend
import jwt
from django.conf import settings
from django.contrib.auth import login,logout, authenticate
from django.conf import settings
import time
from django.contrib import messages


class RegistrationView(View):

    template_name = 'user_templates/1_register.html'
    

    def get(self, request, *args, **kwargs):
        
        if request.user.is_authenticated:
            return redirect('main')

        context={'API_KEY_FETCH':settings.API_KEY_FETCH}

        return render(request, self.template_name, context)


    def post(self, request, *args, **kwargs):
        # Custom input data handling without django forms
        data = request.POST
        email = data['email']
        password1 = data['password1']
        password2 = data['password2']
        name = data['name']
        surname = data['surname']
        '''
            The validation of passwords and email is
            done within html script via Fetch requests
        
        '''
        new_user = CustomUser(
            email = email,
            name = name,
            surname = surname
        )

        new_user.set_password(password1)
        new_user.save()
        
        # #### testing line , delete later ###
        # new_user = CustomUser.objects.get(email="ilnur.karimbek@gmail.com")
        # new_user.name = name
        # new_user.surname = surname
        # new_user.save()
        # ##############################################################
        token = new_user.obtain_tokens()['refresh']
        domain = get_current_site(request).domain
        abs_url = f"http://{domain}/user/activation/?token={token}"
        

        email_data = {
            'subject': f'Confirmation for {name} {surname}',
            'body':'Hello!',
            'to_email':[email],
            'context':{'name':name, 'surname':surname, 'abs_url':abs_url}
        }

        EmailSend.sending(email_data)
        return redirect('main')
        

class ActivateAccount(View):

    def get(self, request, *args, **kwargs):

        token = request.GET['token']

        if not token:
            return redirect('main')
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            user_id = payload['user_id']
            expiration = payload['exp']
            time_now = time.time()

            if time_now>expiration:
                messages.error(request, f"Your token activation is expired. Complete the form to obtain new one")
                return redirect('main')

            user = CustomUser.objects.get(id=user_id)
            user.is_verified=True
            user.save()
            login(request, user)
            return redirect('main')

        except:
            return redirect('main') 


class Logout(View):

    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('main')


class Login(View):

    def get(self, request, *args, **kwargs):
        
        return render(request, 'user_templates/2_login.html')

    
    def post(self, request, *args, **kwargs):
       
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(email=email, password=password)

        if user:
            login(request, user)
            return redirect('main')

        context={'email':email,'password':password,'login_error':True}
        return render(request,'user_templates/2_login.html',context=context)