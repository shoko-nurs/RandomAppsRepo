from django import forms
from .models import CustomUser
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.forms import UserCreationForm  


class RegistrationForm(UserCreationForm):
    # password1 = forms.CharField(widget=forms.PasswordInput(attrs={
    #     'class':'line',
    #     'placeholder':'Enter password'}))

    # password2 = forms.CharField(widget=forms.PasswordInput(attrs={
    #     'class':'line',
    #     'placeholder':'Confirm password'}))
    

    class Meta:
        model = CustomUser
        fields = ('email',)

        # widgets={
        #     'email':forms.EmailInput(attrs={
        #         'class':'line',
        #         'placeholder':'Enter your email'})
        # }

    


    # def clean_password1(self):
    #     password = self.cleaned_data.get('password1')
    #     try: 
    #         validate_password(password)
    #         print("Password is valid")
    #     except forms.ValidationError as Error:
    #         self.add_error('password1', Error)

    #     return password

    
    
    # clean_<fieldname>
    # this method validates only 1 field. Custom validation
    # def clean_email(self):
    #     # Here we check if the email is already registered
    #     email_input = self.cleaned_data.get('email')
    #     email_db = CustomUser.objects.filter(email=email_input)
    #     if email_db.exists():
    #         raise forms.ValidationError("This email is registered(from forms.py)")
        
    #     return email_input

    # this method is used to check all fields in the form
    # def clean(self):

    #     cleaned_data = super().clean()

    #     password1 = cleaned_data.get('password1')
    #     password2 = cleaned_data.get('password2')
    
    #     if password1 != password2:
            
    #         raise forms.ValidationError("Passwords must match(from forms.py)")

        # return cleaned_data