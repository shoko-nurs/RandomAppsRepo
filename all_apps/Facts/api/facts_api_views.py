
from rest_framework import generics
from ..models import Category, Fact
from .facts_serializers import FactSerializer, CategorySerializer
from django.conf import settings
from rest_framework.response import Response
from rest_framework import status

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
    
    'url name = user_categories_fetch'

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
        print(cat_obj, " is saved")
        return Response({"message":new_name}, status=status.HTTP_200_OK)


class AddCategoryFetch(generics.GenericAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_queryset(self):
        return super().get_queryset().filter(user_added=self.request.user)

    
    def post(self, request, *args, **kwargs):
        
        new_category = request.data["new_category"].lower().capitalize()

        if self.get_queryset().filter(category=new_category).exists():
            return Response({'message':"This category is already added"})
        
        new_cat_obj = Category(
            
        )


