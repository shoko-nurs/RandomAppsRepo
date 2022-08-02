from requests import request
from rest_framework import generics
from ..models import Category, Fact
from .facts_serializers import FactSerializer


class FactsAPIVIew(generics.ListAPIView):
    queryset = Fact.objects.all()
    serializer_class = FactSerializer



class FromCategoryAPIView(generics.ListAPIView):
    queryset = Fact.objects.all()
    serializer_class = FactSerializer



    def get_queryset(self):        
        # Getting URL parameters 
        # in the form of /?key1=value1&key2=value2

        params = self.request.query_params

        category = params['category']
        
        if category =='random':
            return super().get_queryset()

        
        queryset = Fact.objects.filter(from_category=category)

        return queryset
    

  