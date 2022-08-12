
from rest_framework.permissions import BasePermission
from ...User.models import CustomUser
from rest_framework import exceptions

class ExternalApiAccess(BasePermission):

    def has_permission(self, request, view):
        params = request.query_params

        api_key = params.get('api_key')

        if not api_key:
            raise exceptions.ValidationError({"message":"Api key is not provided"})
        
        user = CustomUser.objects.filter(api_key=api_key)

        if not user.exists(): 
            raise exceptions.ValidationError({"message":"Api key is not correct"})
        
        return True
    
    def has_object_permission(self, request, view, obj):
        params = request.query_params

        api_key = params.get('api_key')

        if not api_key:
            raise exceptions.ValidationError({"message":"Api key is not provided"})
        
        user = CustomUser.objects.filter(api_key=api_key)

        if not user.exists(): 
            raise exceptions.ValidationError({"message":"Api key is not correct"})
        
        return bool(obj.user_added == user)
