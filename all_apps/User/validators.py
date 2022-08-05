from django.contrib.auth import password_validation
from django.core import exceptions

class RegistrationValidator():


    def __init__(self,data):
        self.email = data['email']
        self.password1 = data['password1']
        self.password2 = data['password2']

    def validate_passwords(self):
        pass
    
