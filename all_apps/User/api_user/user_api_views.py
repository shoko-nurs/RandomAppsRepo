from rest_framework import generics
from ..models import CustomUser
from .user_serializers import RegistrationSerializer
from rest_framework.response import Response
from django.conf import settings
import re



def validate_email(email):
    template = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
    if re.match(template,email):
        return True
    return False



class RegistrationAPIView(generics.GenericAPIView):
    serializer_class = RegistrationSerializer
    def get(self, request, *args, **kwargs):
        return Response({"Get":"works"})

    def post(self, request, *args, **kwargs):
        data = request.data
        serialized_data = self.serializer_class(data=data)
        serialized_data.is_valid(raise_exception=True)

        return Response({'ok':'ok'})


class EmailControlFetch(generics.GenericAPIView):



    def post(self, request, *args, **kwargs):
        data = request.data
        email = data['email']

        if not validate_email(email):
            return Response({"message":"Enter valid email address"})

        qs = CustomUser.objects.filter(email=email)
        if qs.exists():
            return Response({"message":'This email is already registered'})
        
        return Response({'message':'This email is available'})
    
