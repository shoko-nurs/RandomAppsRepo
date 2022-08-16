
from rest_framework.permissions import BasePermission
from django.conf import settings


class POSTApiKeyFetch(BasePermission):

    def has_permission(self, request, view):
        
        
        has_key = bool(request.data.get('api_key_fetch'))
        valid_key = bool(request.data.get('api_key_fetch')==settings.API_KEY_FETCH)
        return bool(has_key and valid_key)
    
    def has_object_permission(self, request, view, obj):
        
        
        has_key = bool(request.data.get('api_key_fetch'))
        valid_key = bool(request.data.get('api_key_fetch')==settings.API_KEY_FETCH)
        
        return bool(has_key and valid_key)


class GETApiKeyFetch(BasePermission):
    
    def has_permission(self, request, view):
        params = request.query_params

        has_key = bool(params['api_key_fetch'])
        valid_key = bool(params['api_key_fetch']==settings.API_KEY_FETCH)
        return bool(has_key and valid_key)
    

    def has_object_permission(self, request, view, obj):
        
        params = request.query_params

        has_key = bool(params['api_key_fetch'])
        valid_key = bool(params['api_key_fetch']==settings.API_KEY_FETCH)
        
        return bool(has_key and valid_key)