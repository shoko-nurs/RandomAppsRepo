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
import datetime

class RegistrationView(View):

    template_name = 'user_templates/1_register.html'
    

    def get(self, request, *args, **kwargs):
        
        if request.user.is_authenticated:
            return redirect('main')

        context = {'api_key_fetch':settings.API_KEY_FETCH}

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
            'context':{
                        'name':name, 
                        'surname':surname, 
                        'abs_url':abs_url,
                        'text':"Click here to activate your account"}
        }

        EmailSend.sending(email_data,'account_activation_reset.html')
        
        context={
                'text_1': "The acount activation link has been sent to your email"

        }
        
        return render(request, 'general_messages.html', context)
        

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
        
            if user.is_verified:
                context = {
                    "text_1":"Account is already activated. You can login"
                }
                return render(request, 'general_messages.html', context)

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

        if user == None:
            context={'email':email,'password':password,'error_message':"Invalid credentials"}
            return render(request,'user_templates/2_login.html',context=context)
        
        

        if not user.is_verified:
            context={'email':email,'password':password,'error_message':'Please use activation link sent to your email to verify your account'}
            return render(request,'user_templates/2_login.html',context=context)
        
        login(request, user)


        ### THis part is required for Go backend
        ### Django creates JWT token and stores it in the cookies
        
        response = redirect('main')
            
        
        
        payload = {
            'exp':datetime.datetime.utcnow()+ datetime.timedelta(days=14,seconds=0),
            'iat':datetime.datetime.utcnow(),
            'id':request.user.id
        }
        token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
        response.set_cookie('jwtkn',token)

        return response
        

class PasswordReset(View):
   
    def get(self, request, *args, **kwargs):
        return render(request, 'user_templates/3_password_reset.html')


    def post(self, request, *args, **kwargs):
        email = request.POST['email']
        user = CustomUser.objects.filter(email=email)
        
        if not user.exists():
            
            context= {
                'email':email,
                'email_error':"Email not found"
            }

            return render(request, 'user_templates/3_password_reset.html', context)

        user=user[0]
        
        token = user.obtain_tokens()['access']
        domain = get_current_site(request).domain
        
        abs_url = f"http://{domain}/user/change_password/?token={token}"
       
        email_data = {
            'subject': f'Password reset for {user.name} {user.surname}',
            'body':'Hello!',
            'to_email':[email],
            'context':{
                        'name':user.name, 
                        'surname':user.surname, 
                        'abs_url':abs_url, 
                        'text':"To reset your password click here"}
            
        }

        EmailSend.sending(email_data,'account_activation_reset.html')
        context = {'email':email}
        return render(request, 'user_templates/4_reset_link_sent.html', context=context)






class ChangePassword(View):
    
    def get(self, request, *args, **kwargs):
        
        token=request.GET.get('token')

        if not token:
            return redirect('main')
        
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        
        user_id = payload['user_id']
        expiration = payload['exp']
        time_now = time.time()

        if time_now>expiration:
            messages.error(request, f"Your token activation is expired. Complete the form to obtain new one")
            return redirect('main')
        
        user = CustomUser.objects.filter(id=user_id)
        
        if user.exists():    
            context={
                        'access':True, 
                        'user_id':user_id,
                        'api_key_fetch': settings.API_KEY_FETCH,
                        'token':token}

            
            return render(request, 'user_templates/5_change_password.html', context=context)

    
    def post(self, request, *args, **kwargs):


        token=request.GET.get('token')

        password = request.POST.get('password1')



        if not password or not token:
            text_1= "Access Denied"
            context = {'text_1':text_1}
            return render(request, 'general_messages.html', context)
            
        
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])

        user_id = payload.get('user_id')
        expiration = payload.get('exp')
        time_now = time.time()

        if time_now>expiration:
            text_1 = "Reset link is no longer valid, request another one"
            return render(request, 'general_messages.html', context)
        
        user = CustomUser.objects.get(id=user_id)
        user.set_password(password)
        user.save()

        context = {
                    'text_1':"Your password has been changed. You now can login",
                    'url': 'login',
                    'a_text':"Login"          
                    }
        
        return render(request, 'general_messages.html', context)
        
        

class DeleteAccount(View):
    
    def get(self, request, *args, **kwargs):
        user = request.user
        logout(request)
        user.delete()
        return redirect('main')
        
    

        