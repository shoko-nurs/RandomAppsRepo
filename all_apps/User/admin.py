from django.contrib import admin
from .models import CustomUser, MessagesBackend

# Register your models here.

admin.site.register(CustomUser)
admin.site.register(MessagesBackend)