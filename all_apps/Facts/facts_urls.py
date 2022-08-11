from django.urls import path
from .facts_views import FactsMainPageView, UserFactsPage
from .api.facts_api_views import (
    FactsAPIVIew, 
    NursFromCategoryApiView,
    UserCategoriesFetch,
    EditCategoryFetch,
    EditCategoryFetch,
    AddCategoryFetch,
    GetFactsFromCatFetch,
    EditFactFetch,
    AddFactFetch,
    GetFirstFacts,
    DeleteFactFetch
    
)


urlpatterns=[

    path('', FactsMainPageView.as_view(), name='facts-main-page'),
    path('user/', UserFactsPage.as_view(),name="user_facts_page" ),

    path('api/all_facts', FactsAPIVIew.as_view(), name='facts-list' ),
    path('api/from/', NursFromCategoryApiView.as_view(), name='from_category' ),
    path('api/user_categories/', UserCategoriesFetch.as_view(), name='user_categories_fetch'),
    path('api/edit_category/', EditCategoryFetch.as_view(), name='edit_category_fetch'),
    path('api/add_category_fetch', AddCategoryFetch.as_view(), name="add_category_fetch"),
    path('api/get_facts_from_cat_fetch',GetFactsFromCatFetch.as_view(), name='get_facts_from_cat_fetch'),
    path('api/edit_fact_fetch', EditFactFetch.as_view(), name="edit_fact_fetch"),
    path('api/add_fact_fetch', AddFactFetch.as_view(), name='add_fact_fetch'),
    path('api/get_first_facts', GetFirstFacts.as_view(), name="get_first_facts"),
    path('api/delete_fact_fetch',DeleteFactFetch.as_view(), name='delete_fact_fetch'),
 
]