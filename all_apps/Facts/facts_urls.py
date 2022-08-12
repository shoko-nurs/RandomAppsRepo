from django.urls import path, include
from .facts_views import FactsMainPageView, UserFactsPage

urlpatterns=[

    path('', FactsMainPageView.as_view(), name='facts-main-page'),
    path('user/', UserFactsPage.as_view(),name="user_facts_page" ),

    path('fetch_api/', include('all_apps.Facts.fetch_api.fetch_urls')),


]