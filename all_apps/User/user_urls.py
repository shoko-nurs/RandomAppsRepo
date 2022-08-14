from django.urls import path, include
from .user_views import (
    RegistrationView,
    ActivateAccount,
    Logout,
    Login,
    PasswordReset,
    ChangePassword
    
    )





urlpatterns=[


    path('registration/', RegistrationView.as_view(), name='register'),
    path('activation/', ActivateAccount.as_view(),name='activation'),
    path('logout/',Logout.as_view(), name='logout'),
    path('login/', Login.as_view(), name='login'),
    path('password_reset/', PasswordReset.as_view(), name='password_reset'),
    path('change_password/', ChangePassword.as_view(), name="change_password"),


    path('fetch_api/', include('all_apps.User.api_user.user_urls_fetch')),


    
    
]