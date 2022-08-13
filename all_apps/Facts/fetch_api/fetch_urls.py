from django.urls import path
from .facts_api_views import *


urlpatterns = [

        path('all_facts', FactsAPIVIew.as_view(), name='facts-list' ),
        path('from/', NursFromCategoryApiView.as_view(), name='from_category' ),
        path('user_categories/', UserCategoriesFetch.as_view(), name='user_categories_fetch'),
        path('edit_category/', EditCategoryFetch.as_view(), name='edit_category_fetch'),
        path('add_category_fetch', AddCategoryFetch.as_view(), name="add_category_fetch"),
        path('delete_category_fetch', DeleteCategoryFetch.as_view(), name='delete_category_fetch'),
        path('get_facts_from_cat_fetch',GetFactsFromCatFetch.as_view(), name='get_facts_from_cat_fetch'),
        path('edit_fact_fetch', EditFactFetch.as_view(), name="edit_fact_fetch"),
        path('add_fact_fetch', AddFactFetch.as_view(), name='add_fact_fetch'),
        path('get_first_facts', GetFirstFacts.as_view(), name="get_first_facts"),
        path('delete_fact_fetch',DeleteFactFetch.as_view(), name='delete_fact_fetch'),
        path('test_fact', TestFactFetch.as_view(), name="test_fact_fetch"),


]