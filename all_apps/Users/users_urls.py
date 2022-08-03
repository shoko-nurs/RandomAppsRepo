from django.urls import path
from .users_views import CheckUserStatus

urlpatterns=[


    path('', CheckUserStatus.as_view(), name='user-main-page'),
    

]