from django.shortcuts import redirect, render
from django.views.generic.base import View
from django.core import exceptions
from django.contrib.sites.shortcuts import get_current_site
from .models import CustomUser
from .utils import EmailSend


class RegistrationView(View):

    template_name = 'user_templates/1_register.html'
    

    def get(self, request, *args, **kwargs):
        
        if request.user.is_authenticated:
            return redirect('main')

        return render(request, self.template_name)


    def post(self, request, *args, **kwargs):
        # Custom input data handling without django forms
        data = request.POST
        email = data['email']
        password1 = data['password1']
        password2 = data['password2']
        
        '''
            The validation of passwords and email is
            done within html script via Fetch requests
        
        '''
        new_user = CustomUser(
            email = email,
            name = 'X',
            surname = 'Y'
        )
        new_user.set_password(password1)
        
        email_data = {
            'subject': f'Confirmation for {email}',
            'body':'Hello!',
            'to_email':[email],
            'context':{'data':123}
        }

        EmailSend.sending(email_data)
        new_user.save()
        print("email sent!")
        return redirect('register')
        

class LogoutView(View):

    def get(self, request, *args, **kwargs):
        pass