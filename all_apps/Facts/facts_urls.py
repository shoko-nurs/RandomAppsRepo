from django.urls import path
from .views import FactsMainPageView

urlpatterns=[

    path('', FactsMainPageView.as_view(), name='facts-main-page'),

]