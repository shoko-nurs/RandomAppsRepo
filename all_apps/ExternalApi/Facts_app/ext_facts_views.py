
from ast import Delete
from unicodedata import category
from rest_framework import generics
from ...Facts.fetch_api.fetch_permissions import POSTApiKeyFetch
from all_apps.Facts.models import Category, Fact
from all_apps.User.models import CustomUser
from all_apps.Facts.facts_serializers import FactSerializer, CategorySerializer,CreateFactSerializer
from .ext_facts_permissions import ExternalApiAccess
from rest_framework import exceptions
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.response import Response


class SwaggerManualParam:
    api_key = openapi.Parameter('api_key',in_=openapi.IN_QUERY,type=openapi.TYPE_STRING)
    @swagger_auto_schema( manual_parameters=[api_key]) 
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


    api_key = openapi.Parameter('api_key',in_=openapi.IN_QUERY,type=openapi.TYPE_STRING)
    @swagger_auto_schema( manual_parameters=[api_key]) 
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    api_key = openapi.Parameter('api_key',in_=openapi.IN_QUERY,type=openapi.TYPE_STRING)
    @swagger_auto_schema( manual_parameters=[api_key]) 
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)


    api_key = openapi.Parameter('api_key',in_=openapi.IN_QUERY,type=openapi.TYPE_STRING)
    @swagger_auto_schema( manual_parameters=[api_key]) 
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)


    api_key = openapi.Parameter('api_key',in_=openapi.IN_QUERY,type=openapi.TYPE_STRING)
    @swagger_auto_schema( manual_parameters=[api_key]) 
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)


class AllCategories( generics.ListAPIView):

    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [ExternalApiAccess]
    authentication_classes = []

    api_key = openapi.Parameter('api_key',in_=openapi.IN_QUERY,type=openapi.TYPE_STRING)
    @swagger_auto_schema( manual_parameters=[api_key]) 
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        api_key = self.request.query_params.get('api_key')
        user = CustomUser.objects.get(api_key=api_key)
        return super().get_queryset().filter(user_added=user)



class ManageCategory( generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [ExternalApiAccess]
    authentication_classes = []
    lookup_field = 'id'


    api_key = openapi.Parameter('api_key',in_=openapi.IN_QUERY,type=openapi.TYPE_STRING)
    @swagger_auto_schema( manual_parameters=[api_key])
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    api_key = openapi.Parameter('api_key',in_=openapi.IN_QUERY,type=openapi.TYPE_STRING)
    @swagger_auto_schema( manual_parameters=[api_key])
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)


    api_key = openapi.Parameter('api_key',in_=openapi.IN_QUERY,type=openapi.TYPE_STRING)
    @swagger_auto_schema( manual_parameters=[api_key])
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

    api_key = openapi.Parameter('api_key',in_=openapi.IN_QUERY,type=openapi.TYPE_STRING)
    @swagger_auto_schema( manual_parameters=[api_key])
    def delete(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)




    def get_queryset(self):
        api_key = self.request.query_params.get('api_key')
        user = CustomUser.objects.get(api_key=api_key)
        return super().get_queryset().filter(user_added=user)   
    


    def get_object(self):
        kwargs = self.kwargs
        if self.kwargs.get('id'):
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


    api_key = openapi.Parameter('api_key',in_=openapi.IN_QUERY,type=openapi.TYPE_STRING)
    @swagger_auto_schema( manual_parameters=[api_key])
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    def perform_create(self, serializer):
        api_key = self.request.query_params.get('api_key')
        try:
            user = CustomUser.objects.get(api_key=api_key)
            serializer.save(user_added=user)
        except:
            raise exceptions.ValidationError({"message":"This category is already added"})


class GetFactsFromCategory(generics.ListAPIView):
    serializer_class = FactSerializer
    queryset = Fact.objects.all()
    permission_classes = [ExternalApiAccess]
    authentication_classes = []

    def get_queryset(self):
        api_key = self.request.query_params.get('api_key')
        user = CustomUser.objects.get(api_key=api_key)

        lookup_field = self.kwargs.get('id') or self.kwargs.get('category')
        
        if lookup_field and lookup_field.isdigit():
            cat_obj = Category.objects.filter(id=lookup_field, user_added=user)
            if cat_obj.exists():
                qs = super().get_queryset().filter(from_category=cat_obj[0])
                return qs
            raise exceptions.ValidationError({"message":"No such category"})
        
        lookup_field = lookup_field.lower().capitalize()
        cat_obj = Category.objects.filter(category=lookup_field, user_added=user)
        if cat_obj.exists():
            qs = super().get_queryset().filter(from_category=cat_obj[0])
            return qs
        raise exceptions.ValidationError({"message":"No such category"})


    api_key = openapi.Parameter('api_key',in_=openapi.IN_QUERY,type=openapi.TYPE_STRING)
    @swagger_auto_schema( manual_parameters=[api_key])
    def get(self, request, *args, **kwargs):
        qs = self.get_queryset()
        serialized_data = self.get_serializer(qs, many=True)
        return Response(serialized_data.data)


class DeleteFactsFromCategory(generics.GenericAPIView):
    serializer_class = FactSerializer
    queryset = Fact.objects.all()
    permission_classes = [ExternalApiAccess]
    authentication_classes = []

    def get_queryset(self):
        api_key = self.request.query_params.get('api_key')
        user = CustomUser.objects.get(api_key=api_key)

        lookup_field = self.kwargs.get('id') or self.kwargs.get('category')
       
        if lookup_field and lookup_field.isdigit():
            cat_obj = Category.objects.filter(id=lookup_field, user_added=user)
            
        else:   
            lookup_field = lookup_field.lower().capitalize()
            cat_obj = Category.objects.filter(category=lookup_field, user_added=user)           
            
            if cat_obj.exists():
                qs = super().get_queryset().filter(from_category=cat_obj[0])
                cat_name = cat_obj[0].category
                return [qs, cat_name]
            raise exceptions.ValidationError({"message":"No such category"})
        

    api_key = openapi.Parameter('api_key',in_=openapi.IN_QUERY,type=openapi.TYPE_STRING)
    @swagger_auto_schema( manual_parameters=[api_key])
    def delete(self, request, *args, **kwargs):
        qs, cat_name = self.get_queryset() 
        qs.delete()
        return Response({"message":f"All facts from {cat_name} are deleted"})



class ManageFact(generics.RetrieveUpdateDestroyAPIView):
    queryset = Fact.objects.all()
    serializer_class = FactSerializer
    permission_classes = [ExternalApiAccess]
    authentication_classes = []
    lookup_field = 'id'

    # def get_queryset(self):
    #     api_key = self.request.query_params.get('api_key')
    #     user = CustomUser.objects.get(api_key=api_key)
    #     return super().get_queryset().filter(user_added=user)


    api_key = openapi.Parameter('api_key',in_=openapi.IN_QUERY,type=openapi.TYPE_STRING)
    @swagger_auto_schema( manual_parameters=[api_key])
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    api_key = openapi.Parameter('api_key',in_=openapi.IN_QUERY,type=openapi.TYPE_STRING)
    @swagger_auto_schema( manual_parameters=[api_key])
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    api_key = openapi.Parameter('api_key',in_=openapi.IN_QUERY,type=openapi.TYPE_STRING)
    @swagger_auto_schema( manual_parameters=[api_key])
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)


    api_key = openapi.Parameter('api_key',in_=openapi.IN_QUERY,type=openapi.TYPE_STRING)
    @swagger_auto_schema( manual_parameters=[api_key])
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)



class CreateFact(generics.CreateAPIView):
    serializer_class = CreateFactSerializer
    queryset = Category
    authentication_classes = []
    permission_classes = [ExternalApiAccess]


    def perform_create(self, serializer):

        api_key = self.request.query_params.get('api_key')
        cat_id = self.request.data.get('from_category')
        cat_obj = Category.objects.get(id=cat_id)
        user = CustomUser.objects.get(api_key=api_key)
        
        if cat_obj.user_added == user:
            serializer.save(user_added=user)
        raise exceptions.ValidationError("No such category")



    api_key = openapi.Parameter('api_key',in_=openapi.IN_QUERY,type=openapi.TYPE_STRING)
    @swagger_auto_schema( manual_parameters=[api_key])
    def post(self, request, *args, **kwargs):   
        return super().post(request, *args, **kwargs)
