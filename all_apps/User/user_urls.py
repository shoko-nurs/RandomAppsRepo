from django.urls import path
from .user_views import (
    RegistrationView,
    ActivateAccount,
    Logout,
    Login,
    PasswordReset,
    ChangePassword
    
    )


from .api_user.user_fetch_api_views import ( 
    EmailControlCSRf,
    LoginControl,
    Password1Control,
    Password2Control,
    
    )


urlpatterns=[


    path('registration/', RegistrationView.as_view(), name='register'),
    path('activation/', ActivateAccount.as_view(),name='activation'),
    path('logout/',Logout.as_view(), name='logout'),
    path('login/', Login.as_view(), name='login'),
    path('passoword_reset/', PasswordReset.as_view(), name='password_reset'),
    path('change_password/', ChangePassword.as_view(), name="change_password"),


    #path('api/registration/', RegistrationAPIView.as_view(), name='registration_api'),    
    path('api/email_control_fetch/', EmailControlCSRf, name='email_control_fetch'),
    path('api/password1_contol_fetch/', Password1Control.as_view() , name='password1_control_fetch'),
    path('api/password2_control_fetch/', Password2Control.as_view(), name='password2_control_fetch'),
    
]