
from rest_framework import generics
from ..models import CustomUser
from .user_serializers import RegistrationSerializer
from rest_framework.response import Response
from django.conf import settings
from django.contrib.auth import password_validation
import re
from django.contrib.auth import login,logout, authenticate
from .user_permissions import POSTApiKeyFetch
from all_apps.User.api_user.user_serializers import ApiKeySerializer
from rest_framework.permissions import IsAuthenticated

def validate_email(email):
    template = "^[a-zA-Z0-9-_.]+@[a-zA-Z0-9]+\.[a-z-.]{1,20}$"
    if re.match(template,email):
        return True
    return False



class EmailControl(generics.GenericAPIView):
    permission_classes = [POSTApiKeyFetch]
    authentication_classes = []

    def post(self, request, *args, **kwargs):
        data = request.data
       
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
    permission_classes = [POSTApiKeyFetch]
    authentication_classes = []

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
    permission_classes = [POSTApiKeyFetch]
    authentication_classes = []

    def post(sellf, request, *args, **kwargs):
        data = request.data
        password1 = data['password1']
        password2 = data['password2']
        api_key_fetch = data['api_key_fetch']


        if not api_key_fetch or api_key_fetch != settings.API_KEY_FETCH:
            return Response({'message':'Error'})

        if not password2:
            return Response({"message":"Confirm your password"})
        
        if password1!=password2:
            return Response({"message":"Passwords must match"})
        
        return Response({"message":"OK"})


class LoginControl(generics.GenericAPIView):
    permission_classes = [POSTApiKeyFetch]
    authentication_classes = []

    def post(self, request, *args, **kwargs):

        data = request.data 
        email = data['email']
        password = data['password']
        
        user  = authenticate(email=email, password=password)
        if not user:
            return Response({"message":"Invalid username or password"})
        
        return Response({"message":"OK"})


class ManageApiKey(generics.GenericAPIView):
    serializer_class = ApiKeySerializer
    permission_classes=[IsAuthenticated]
    
    def get(self, request, *args, **kwargs):
        request.user.claim()
        user = request.user
        serialized_data = self.get_serializer(user, many=False)
        return Response({"message":"OK", "data":user.api_key})    


