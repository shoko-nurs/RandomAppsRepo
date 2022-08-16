from xmlrpc.client import ResponseError
from django.shortcuts import render
from django.views.generic.base import View
from django.conf import settings
from rest_framework import generics
from rest_framework.response import Response
from all_apps.User.api_user.user_permissions import POSTApiKeyFetch
import re

def validate_email(email):
    template = "^[a-zA-Z0-9-_.]+@[a-zA-Z0-9]+\.[a-z-.]{1,20}$"
    if re.match(template,email):
        return True
    return False


def main(request):
    context={'123':123}
    return render(request, 'main_page.html' , context)



class LeaveMessage(View):

    def get(self, request, *args, **kwargs):
        context = {'api_key_fetch':settings.API_KEY_FETCH}
        return render(request, 'message.html', context)




class MessageEmailControl(generics.GenericAPIView):
    authentication_classes=[]
    permission_classes = [POSTApiKeyFetch]
    def post(self, request, *args, **kwargs):

        email = request.data['email']
        if not email:
            return Response({'message':"Can't be blank"})



        if not validate_email(email):
            return Response({'message':"Enter valid email address"})
        
        return Response({'message':"OK"})
        
