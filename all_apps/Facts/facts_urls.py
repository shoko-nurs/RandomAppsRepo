from django.urls import path
from .facts_views import FactsMainPageView
from .api.facts_api_views import FactsAPIVIew, FromCategoryAPIView

urlpatterns=[

    path('', FactsMainPageView.as_view(), name='facts-main-page'),
    path('api/all_facts', FactsAPIVIew.as_view(), name='facts-list' ),
    path('api/from_category/', FromCategoryAPIView.as_view(), name='from_category' ),
]