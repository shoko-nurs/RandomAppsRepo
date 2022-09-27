from rest_framework import serializers
from all_apps.User.models import CustomUser



class TeacherInfoSerializer(serializers.ModelSerializer):


    class Meta:
        model = CustomUser
        fields = ['name', 'surname']

        