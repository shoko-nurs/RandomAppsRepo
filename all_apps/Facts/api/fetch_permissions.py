from rest_framework.permissions import BasePermission, IsAuthenticated
from django.conf import settings


class ApiKeyFetchAuthenticated(BasePermission):

    def has_permission(self, request, view):
        
        user = request.user.is_authenticated
        has_key = bool(request.data['api_key_fetch'])
        valid_key = bool(request.data['api_key_fetch'])
        return bool(user and has_key and valid_key)
    
    def has_object_permission(self, request, view, obj):
        
        user = request.user.is_authenticated
        has_key = bool(request.data['api_key_fetch'])
        valid_key = bool(request.data['api_key_fetch'])
        return bool(user and has_key and valid_key)