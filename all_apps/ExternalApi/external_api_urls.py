
from django.urls import path, include
from .swagger_urls import schema_view


urlpatterns=[

   path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
   path('facts_api/', include('all_apps.ExternalApi.Facts_app.ext_facts_urls')),
]




