"""RandomApps URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from .main_views import main,LeaveMessage,MessageEmailControl,SubmitMessageBackend


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main , name='main'),
    path('message/', LeaveMessage.as_view(), name='message'),
    
    path('facts/', include('all_apps.Facts.facts_urls')),
    path('user/', include('all_apps.User.user_urls')),
    path('api_documentation/', include('all_apps.ExternalApi.external_api_urls')),

    path('student_merit/', include('all_apps.StudentMerit.merit_urls')),
    
    # For message
    path('message_email_conrol/', MessageEmailControl.as_view(), name="message_email_control"),
    path('submit_message/', SubmitMessageBackend.as_view(), name="submit_message_backend"),
]

