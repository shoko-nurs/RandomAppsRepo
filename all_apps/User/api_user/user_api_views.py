from unittest import result
from rest_framework import generics
from rest_framework.views import APIView
from ..models import CustomUser
from .user_serializers import RegistrationSerializer
from rest_framework.response import Response
from django.conf import settings
from django.contrib.auth import password_validation
import re



def validate_email(email):
    template = "^[a-zA-Z0-9-_.]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
    if re.match(template,email):
        return True
    return False



class RegistrationAPIView(generics.GenericAPIView):
    
    serializer_class = RegistrationSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        serialized_data = self.serializer_class(data=data)
        serialized_data.is_valid(raise_exception=True)

        return Response({'ok':'ok'})


class EmailControl(generics.GenericAPIView):
    

    def post(self, request, *args, **kwargs):
        data = request.data
        print(data)
        email = data['email']
        if not email:
            return Response({'message':'Email can not be blank'})

        if not validate_email(email):
            return Response({"message":"Enter valid email address"})

        qs = CustomUser.objects.filter(email=email)
        if qs.exists():
            return Response({"message":'This email is already registered'})
        
        return Response({'message':'OK'})


class Password1Control(generics.GenericAPIView):
    
    def post(self, request, *args, **kwargs):
        data = request.data
        password = data['password1']
        
        
        if not password or password=="":
            return Response({"message":["Password can not be blank"]})
        
        try:
            password_validation.validate_password(password) 
            
            return Response({"message":"OK"})

        except Exception as e:
            return Response({"message":e})


class Password2Control(generics.GenericAPIView):

    def post(sellf, request, *args, **kwargs):
        data = request.data
        password1 = data['password1']
        password2 = data['password2']

        if not password2:
            return Response({"message":"Confirm your password"})
        
        if password1!=password2:
            return Response({"message":"Passwords must match"})
        
        return Response({"message":"OK"})
