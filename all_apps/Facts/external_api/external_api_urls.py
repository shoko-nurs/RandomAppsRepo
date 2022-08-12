from django.urls import path
from .external_api_views import AllCategories, GetCategory


urlpatterns = [

    path('all_categories/', AllCategories.as_view(), name="get_categories_api"),
    path('category/<int:id>', GetCategory.as_view(), name="get_category"),





]