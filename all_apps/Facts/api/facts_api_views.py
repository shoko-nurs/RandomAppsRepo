
from rest_framework import generics
from ..models import Category, Fact
from .facts_serializers import FactSerializer, CategorySerializer
from django.conf import settings
from rest_framework.response import Response

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
    


"AJHRU873AHbHAUW74nAbvAjbw38gbAbiab37y3948024bakbbbwiAbhdb89"

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
       