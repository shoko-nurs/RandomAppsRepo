from email import message
from rest_framework import serializers
from all_apps.User.models import MessagesBackend
from rest_framework import exceptions


class MessageBackendSerializer(serializers.ModelSerializer):

    class Meta:
        model = MessagesBackend
        fields = ['from_email', 'message']
