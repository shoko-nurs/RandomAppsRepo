from multiprocessing import context
from django.shortcuts import redirect, render
from django.views.generic.base import View
from .user_forms import RegistrationForm
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions


class RegistrationView(View):

    template_name = 'user_templates/1_register.html'
    

    def get(self, request, *args, **kwargs):
        form = RegistrationForm
        
        return render(request, self.template_name)


    def post(self, request, *args, **kwargs):
        # Custom input data handling without django forms
        data = request.POST
        email = data['email']
        password1 = data['password1']
        password2 = data['password2']
        print(data)
        # validate password
        return redirect('register')
        

class LogoutView(View):

    def get(self, request, *args, **kwargs):
        pass