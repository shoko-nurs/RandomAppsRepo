from django.urls import path
from .external_api_views import AllCategories, EditCategory


urlpatterns = [

    path('all_categories/', AllCategories.as_view(), name="get_categories_api"),
    path('edit_category/', EditCategory.as_view(), name="edit_category"),





]