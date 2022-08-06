from django.urls import path
from .user_views import RegistrationView
from .api_user.user_api_views import (
    RegistrationAPIView, 
    EmailControl,
    Password1Control,
    Password2Control)


urlpatterns=[


    path('registration/', RegistrationView.as_view(), name='register'),
    
    #path('api/registration/', RegistrationAPIView.as_view(), name='registration_api'),    
    path('api/email_control_fetch/', EmailControl.as_view(), name='email_control_fetch'),
    path('api/password1_contol_fetch/', Password1Control.as_view() , name='password1_control_fetch'),
    path('api/password2_control_fetch/', Password2Control.as_view(), name='password2_control_fetch'),
    
]