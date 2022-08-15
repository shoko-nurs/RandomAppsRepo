from django.urls import path
from .user_fetch_api_views import(
    EmailControl,
    Password1Control,
    Password2Control,
    ManageApiKey
)



urlpatterns = [


    path('email_control_fetch/', EmailControl.as_view(), name='email_control_fetch'),
    path('password1_contol_fetch/', Password1Control.as_view() , name='password1_control_fetch'),
    path('password2_control_fetch/', Password2Control.as_view(), name='password2_control_fetch'),
    path('manage_api_key', ManageApiKey.as_view(), name="manage_api_key"),


]