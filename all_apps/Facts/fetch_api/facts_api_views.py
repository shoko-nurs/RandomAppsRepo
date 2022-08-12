
from pickletools import read_uint1
from unicodedata import category
from rest_framework import generics
from ..models import Category, Fact
from ..facts_serializers import FactSerializer, CategorySerializer
from django.conf import settings
from rest_framework.response import Response
from rest_framework import status
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .fetch_permissions import GETApiKeyFetch, POSTApiKeyFetch
import random


class FactsAPIVIew(generics.ListAPIView):
    queryset = Fact.objects.all()
    serializer_class = FactSerializer



class NursFromCategoryApiView(generics.ListAPIView):
    queryset = Fact.objects.filter(user_added=1)
    serializer_class = FactSerializer
    permission_classes=[]

    def get_queryset(self):        
        # Getting URL parameters 
        # in the form of /?key1=value1&key2=value2

        params = self.request.query_params

        
        category = params['category']
        
        if category =='random':
            return super().get_queryset()

        
        queryset = super().get_queryset().filter(from_category=category)

        return queryset
    




class UserCategoriesFetch(generics.GenericAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    

    def get_queryset(self):
        return super().get_queryset().filter(user_added=self.request.user)

    def get(self, request, *args, **kwargs):
        params = self.request.query_params

        api_key_fetch = params.get('api_key_fetch')

        
        if api_key_fetch==None or (api_key_fetch!=settings.API_KEY_FETCH):
            return Response({"message":"Error"})
        

        qs = self.get_queryset()
        serialized_data = self.get_serializer(qs, many=True)
        return Response(serialized_data.data)

    

class EditCategoryFetch(generics.GenericAPIView):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # Auth class is empty because DRF enforces the use of CSRF tokens
    # if the default authentication is SessionAuthentication
    # for this reason I remove csrf check for now.
    # However, api key will be used 
    

    def get_queryset(self):
        return super().get_queryset().filter(user_added=self.request.user)
        


    def post(self, request, *args, **kwargs):
        
        api_key_fetch = request.data['api_key_fetch']
        
        if not api_key_fetch or api_key_fetch!=settings.API_KEY_FETCH:
            return Response({"message":"Error"})

        old_name = request.data['old_name'].lower().capitalize()
        new_name = request.data['new_name'].lower().capitalize()


        if old_name == new_name:
            return Response({'message': old_name})

        cat_obj = self.get_queryset().get(category=old_name)
        
        if self.get_queryset().filter(category=new_name).exists():
            return Response({'message':'This category already exists',
                             'status':status.HTTP_406_NOT_ACCEPTABLE} )

        cat_obj.category = new_name
        cat_obj.save()
       
        return Response({"message":new_name}, status=status.HTTP_200_OK)


class AddCategoryFetch(generics.GenericAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_queryset(self):
        return super().get_queryset().filter(user_added=self.request.user)

    
    def post(self, request, *args, **kwargs):
        
        api_key_fetch = request.data["api_key_fetch"]
        if not api_key_fetch or api_key_fetch!=settings.API_KEY_FETCH:
            return Response({"message":"Access Denied"})


        new_category = request.data["new_category"].lower().capitalize()


        if self.get_queryset().filter(category=new_category).exists():
            return Response({'message':"This category is already added"})
        
        
        new_cat_obj = Category(
            category=new_category,
            user_added = request.user

        )

        new_cat_obj.save()
        return Response({"message":"OK"})


class GetFactsFromCatFetch(generics.GenericAPIView):
    queryset =Fact.objects.all()    
    serializer_class = FactSerializer

    def get_queryset(self):
        return super().get_queryset().filter(user_added=self.request.user)

    def get(self, *args, **kwargs):
        
        params = self.request.query_params

        api_key_fetch = params.get('api_key_fetch')
        category = params.get('category')
        
        if api_key_fetch==None or (api_key_fetch!=settings.API_KEY_FETCH):
            return Response({"message":"Error"})
        
        try:
            cat_obj = Category.objects.get(category=category)

            qs = self.get_queryset().filter(from_category=cat_obj)
            serialized_data = self.get_serializer(qs, many=True)
            return Response({"message":"OK", "data":serialized_data.data})
        
        except:
            return Response({"message":"No category"})


class EditFactFetch(generics.GenericAPIView):

    queryset = Fact.objects.all()
    serializer_class = FactSerializer

    def get_queryset(self):
        return super().get_queryset().filter(user_added=self.request.user)

    def post(self, request, *args, **kwargs):

        api_key_fetch = request.data['api_key_fetch']
        if not api_key_fetch or api_key_fetch!=settings.API_KEY_FETCH:
            return Response({"message":"Access Denied"})

        edited_fact = request.data['edited_fact']
        old_fact = request.data['old_fact']

        if edited_fact == old_fact:
            return Response({"message":edited_fact})

        fact_obj = self.get_queryset().get(fact=old_fact)
        fact_obj.fact = edited_fact
        fact_obj.save()
        return Response({"message":edited_fact})


class AddFactFetch(generics.GenericAPIView):
    queryset = Fact.objects.all()
    serializer_class = FactSerializer
    permission_classes=[POSTApiKeyFetch]
    

    def post(self, request, *args, **kwargs):
   
        new_fact = request.data['new_fact']
        selected_category = request.data['selected_category']

        cat_obj = Category.objects.get(category=selected_category)
        
        if Fact.objects.filter(fact=new_fact, from_category=cat_obj):
            return Response({"message":"Exact same fact is already present"})

        new_fact_obj = Fact(

            from_category =cat_obj ,
            fact = new_fact,
            user_added = request.user
        )

        new_fact_obj.save()

        return Response({"message":"OK"})


class DeleteFactFetch(generics.GenericAPIView):
    queryset = Fact.objects.all()


    def get_queryset(self):
        return super().get_queryset().filter(user_added=self.request.user)


    def delete(self, request, *args, **kwargs):

        api_key_fetch = request.data['api_key_fetch']
        if not api_key_fetch or api_key_fetch!=settings.API_KEY_FETCH:
            return Response({"message":"Access Denied"})


        fact_id = request.data['fact_id']
        fact_obj = self.get_queryset().get(id=fact_id)
        fact_obj.delete()
        return Response({"message":"OK"})


class GetFirstFacts(generics.GenericAPIView):
    queryset = Category.objects.all()
    serializer_class = FactSerializer

    def get_queryset(self):
        return super().get_queryset().filter(user_added=self.request.user)


    def get(self, request, *args, **kwargs):
        if len(self.get_queryset())!=0:
            last_cat = self.get_queryset()[0]
            
            all_facts = last_cat.all_facts.all()
            serialized_data = self.get_serializer(all_facts, many=True)
            return Response({"message":"OK","data":serialized_data.data})
        return Response({"message":"No facts"})




class TestFactFetch(generics.GenericAPIView):
    queryset = Fact.objects.all()
    permission_classes = [GETApiKeyFetch]
    serializer_class = FactSerializer

    def get_queryset(self):
        return super().get_queryset().filter(user_added=self.request.user)

    def get(self, request, *args, **kwargs):
        params = request.query_params
        selected_category = params['selected_category']
      
        
        if selected_category=="Random":
            total_facts = len(self.get_queryset())

            if total_facts==0:
                return Response({"message":"Empty"})
            
            rand_int = random.randint(0, total_facts-1)

            qs = self.get_queryset()[rand_int]
            serialized_data = self.get_serializer(qs, many=False)
            return Response({"message":"OK", "data":serialized_data.data})


        cat_obj = Category.objects.get(category=selected_category)
        facts = cat_obj.all_facts.all()
        total_facts = len(facts)
 
        if total_facts==0:
            return Response({"message":"Empty"})

        rand_int = random.randint(0, total_facts-1)
        qs = facts[rand_int]
        serialized_data = self.get_serializer(qs, many=False)
        return Response({"message":"OK", "data":serialized_data.data})


