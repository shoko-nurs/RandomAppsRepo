from django.urls import path
from .ext_facts_views import *


urlpatterns = [

    path('all_categories/', AllCategories.as_view(), name="get_categories_api"),
    
    # Getting category instance by ID or by naming
    path('category/<int:id>', GetCategory.as_view(), name="get_category"),
    path('category/<str:category>', GetCategory.as_view(), name="get_category"),
    
    # Creating Category
    path('create_category/', CreateCategory.as_view(), name="create_category"),


    #Get facts from category
    path('get_facts_from/<int:id>', GetFactsFromCategory.as_view(), name="get_facts_from_category"),
    path('get_facts_from/<str:category>', GetFactsFromCategory.as_view(), name="get_facts_from_category"),



]