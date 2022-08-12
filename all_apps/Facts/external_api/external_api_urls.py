from django.urls import path
from .external_api_views import *


urlpatterns = [

    path('all_categories/', AllCategories.as_view(), name="get_categories_api"),
    
    # Getting category instance by ID or by naming
    path('category/<int:id>', GetCategory.as_view(), name="get_category"),
    path('category/<slug:category>', GetCategory.as_view(), name="get_category"),
    
    # Creating Category
    path('create_category/', CreateCategory.as_view(), name="create_category")




]