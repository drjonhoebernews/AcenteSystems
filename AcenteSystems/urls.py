from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Sigorta Systems API",
        default_version='v1',
        description="Sigorta Acentesi API dokümantasyonu",
        terms_of_service="https://cmapi.com.tr/terms/",
        contact=openapi.Contact(email="contact@cmapps.com.tr"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('testyonetim/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    # Diğer URL tanımlamalarınız...

    path('api/users/', include('Users.urls')),
    path('api/vehicles/', include('Vehicles.urls')),
    path('api/policies/', include('Policies.urls')),
    path('api/towtrucks/', include('Towtrucks.urls')),
    path('api/notifications/', include('Notifications.urls')),
    path('api/reviews/', include('Reviews.urls')),
    path('api/campaigns/', include('Campaigns.urls')),
    path('api/faqs/', include('Faqs.urls')),
]
