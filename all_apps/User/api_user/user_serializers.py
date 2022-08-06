from rest_framework import serializers
from django.contrib.auth import password_validation
from django.forms import ValidationError
from ..models import CustomUser

class RegistrationSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(
        max_length=100, 
        write_only=True, 
        required=True, 
        validators=[password_validation.validate_password],
        style={'input_type':'password'}
    )

    password2 = serializers.CharField(
        max_length=100, 
        write_only=True, 
        required=True, 
        validators=[password_validation.validate_password],
        style={'input_type':'password'}
    )

    class Meta:
        model = CustomUser
        fields=['email','password1','password2']
    
    def validate(self, attrs):
        password1 = attrs.get('password1')
        password2 = attrs.get('password2')


        if (password1 and password2) and password1!=password2:
            raise ValidationError({"error":"Passwords must match"})

        return attrs
    
    def create(self, validated_data):
        new_user = CustomUser(
            email = validated_data['email'],
            name = 'X',
            surname = 'Y'
        )
        new_user.set_password(validated_data['password1'])
        new_user.save()
        return new_user