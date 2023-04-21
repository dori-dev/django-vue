"""config URL Configuration
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="Simple Blog API",
        default_version='v1',
        description="The simple blog api.",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="mr.dori.dev@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('', schema_view.with_ui('redoc', cache_timeout=0), name='redoc'),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls', namespace='api')),
    path('api/auth/', include('djoser.urls')),
    path('api/auth/', include('djoser.urls.authtoken')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger'),
]
