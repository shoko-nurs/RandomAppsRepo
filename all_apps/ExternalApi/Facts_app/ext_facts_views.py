
from rest_framework import generics
from all_apps.Facts.models import Category, Fact
from all_apps.User.models import CustomUser
from all_apps.Facts.facts_serializers import FactSerializer, CategorySerializer
from .ext_facts_permissions import ExternalApiAccess
from rest_framework import exceptions


class AllCategories( generics.ListAPIView):

    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [ExternalApiAccess]


    def get_queryset(self):
        api_key = self.request.query_params.get('api_key')
        user = CustomUser.objects.get(api_key=api_key)
        return super().get_queryset().filter(user_added=user)



class GetCategory( generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [ExternalApiAccess]



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