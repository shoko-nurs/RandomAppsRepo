from unicodedata import category
from rest_framework import serializers
from  .models import Fact, Category


class FactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Fact
        fields= '__all__'


class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields= '__all__'
        read_only_fields =['user_added']
    
    def validate(self, attrs):
        category = attrs['category']
        print(category)
        return super().validate(attrs)