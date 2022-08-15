
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Facts API",
      default_version='v1',
      description="Test API with your key",
    #   terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="shokonurs@gmail.com"),
      
   ),

   patterns= [path('api_documentation/', include('all_apps.ExternalApi.external_api_urls')),],
   public=True,
   permission_classes=[permissions.IsAuthenticated],
)


urlpatterns=[

   path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
   path('facts_api/', include('all_apps.ExternalApi.Facts_app.ext_facts_urls')),


]




