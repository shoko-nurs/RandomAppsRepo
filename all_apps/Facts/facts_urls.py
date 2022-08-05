from django.urls import path
from .facts_views import FactsMainPageView, UserFactsPage
from .api.facts_api_views import FactsAPIVIew, NursFromCategoryApiView

urlpatterns=[

    path('', FactsMainPageView.as_view(), name='facts-main-page'),
    path('user/', UserFactsPage.as_view(),name="user_facts_page" ),
    
    path('api/all_facts', FactsAPIVIew.as_view(), name='facts-list' ),
    path('api/from/', NursFromCategoryApiView.as_view(), name='from_category' ),
]