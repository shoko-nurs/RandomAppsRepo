
from rest_framework import generics
from ..models import Category, Fact
from .facts_serializers import FactSerializer


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
    

  