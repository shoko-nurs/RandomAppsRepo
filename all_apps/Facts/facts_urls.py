from django.urls import path
from .facts_views import FactsMainPageView

urlpatterns=[

    path('', FactsMainPageView.as_view(), name='facts-main-page'),

]