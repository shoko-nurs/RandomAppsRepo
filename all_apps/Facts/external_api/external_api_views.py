from asyncio import mixins
from rest_framework import generics
from ..models import Category, Fact
from ...User.models import CustomUser
from ..facts_serializers import FactSerializer, CategorySerializer
from .external_api_permissions import ExternalApiAccess



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
    lookup_field = "id"



    def get_queryset(self):
        api_key = self.request.query_params.get('api_key')
        user = CustomUser.objects.get(api_key=api_key)
        return super().get_queryset().filter(user_added=user)   