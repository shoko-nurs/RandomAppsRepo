from lib2to3.pytree import Base
from locale import normalize
from typing import Type
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin


class UserManager(BaseUserManager):

    def create_user(self, email, name, surname, password):

        if not email:
            raise TypeError("Please provide email")
        
        if not name:
            raise TypeError("Please provide your name")
        
        if not surname:
            raise TypeError("Please provide your surname")

        if not password:
            raise TypeError("Please provide your NEW password")
        
        new_user = self.model(

            email=self.normalize_email(email),
            name=name,
            surname=surname

        )

        new_user.set_password(password)
        new_user.is_active = True
        new_user.save()
        return new_user
    
    def create_superuser(self, email, name, surname, password):
        if password == None:
            raise TypeError("Please provide password")
        
        user = self.create_user(email, name, surname, password)
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        user.is_verified = True
        user.save()
        return user

class CustomUser(AbstractBaseUser, PermissionsMixin):

    name = models.CharField(max_length=50, blank=False, null=False)
    surname = models.CharField(max_length=60, blank=False, null=False)
    email = models.EmailField(unique=True, blank=False, null=False)
    join_date = models.DateTimeField(auto_now_add=True)

    
    server_token = models.CharField(max_length=300, blank=True)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    api_key = models.CharField(max_length=6,unique=True, null=True, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['name', 'surname']

    objects = UserManager()

    def __str__(self):
        return f" {self.name} {self.surname}"
        