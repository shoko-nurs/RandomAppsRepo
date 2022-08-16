from django.urls import path
from .ext_facts_views import *


urlpatterns = [

    path('all_categories/', AllCategories.as_view(), name="get_categories_api"),
    
    # Getting category instance by ID or by naming
    path('manage_category/<int:id>', ManageCategory.as_view(), name="get_category"),
    path('manage_category/<str:category>', ManageCategory.as_view(), name="get_category"),
    

    # Creating Category
    path('create_category/', CreateCategory.as_view(), name="create_category"),


    #Get facts from category
    path('get_facts_from/<int:id>', GetFactsFromCategory.as_view(), name="get_facts_from_category"),
    path('get_facts_from/<str:category>', GetFactsFromCategory.as_view(), name="get_facts_from_category"),

    path('delete_all_facts_from/<int:id>', DeleteFactsFromCategory.as_view(),name="delete_facts_from_category"),
    path('delete_all_facts_from/<str:category>', DeleteFactsFromCategory.as_view(),name="delete_facts_from_category"),
    path('manage_fact/<int:id>', ManageFact.as_view(), name="manage_fact"),
    path('create_fact/', CreateFact.as_view(), name="create_fact"),

]
