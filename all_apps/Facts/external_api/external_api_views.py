from asyncio import mixins
from logging import exception
from unicodedata import category
from rest_framework import generics
from ..models import Category, Fact
from ...User.models import CustomUser
from ..facts_serializers import FactSerializer, CategorySerializer
from .external_api_permissions import ExternalApiAccess
from rest_framework import exceptions


class AllCategories( generics.ListAPIView):

    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [ExternalApiAccess]
    authentication_classes = []

    def get_queryset(self):
        api_key = self.request.query_params.get('api_key')
        user = CustomUser.objects.get(api_key=api_key)
        return super().get_queryset().filter(user_added=user)



class GetCategory( generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [ExternalApiAccess]
    authentication_classes = []


    def get_queryset(self):
        api_key = self.request.query_params.get('api_key')
        user = CustomUser.objects.get(api_key=api_key)
        return super().get_queryset().filter(user_added=user)   
    
    def get_object(self):
        kwargs = self.kwargs
        
        if kwargs.get('id'):
            return super().get_object()
        
        else:
            category = kwargs['category'].lower().capitalize()
            qs = Category.objects.filter(category=category)
            if not qs:
                raise exceptions.ValidationError({"message":"No such category"})
            
            return qs[0]




class CreateCategory(generics.CreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [ExternalApiAccess]
    authentication_classes = []

    def perform_create(self, serializer):
        api_key = self.request.query_params.get('api_key')
        try:
            user = CustomUser.objects.get(api_key=api_key)
            serializer.save(user_added=user)
        except:
            raise exceptions.ValidationError({"message":"This category is already added"})