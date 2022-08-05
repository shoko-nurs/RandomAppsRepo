from django.urls import path
from .user_views import RegistrationView
from .api_user.user_api_views import RegistrationAPIView, EmailControlFetch

urlpatterns=[


    path('', RegistrationView.as_view(), name='register'),
    path('api/registration/', RegistrationAPIView.as_view(), name='registration_api'),
    
    path('api/email_control_fetch/', EmailControlFetch.as_view(), name='email_control_fetch'),
]