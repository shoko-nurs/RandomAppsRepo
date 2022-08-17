from dataclasses import field
from unicodedata import category
from rest_framework import serializers
from  .models import Fact, Category


class FactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Fact
        fields= '__all__'
        read_only_fields=['user_added','from_category']


class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields= '__all__'
        read_only_fields =['user_added']
    


class CreateFactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fact
        fields='__all__'
        read_only_fields = ['user_added','from_category']
        