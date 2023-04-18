"""config URL Configuration
"""
from django.contrib import admin
from django.urls import path, include
from dj_rest_auth.views import PasswordResetConfirmView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls', namespace='blog')),
    path('api/', include('api.urls', namespace='api')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/rest-auth/', include('dj_rest_auth.urls')),
    path(
        'api/rest-auth/registration/',
        include('dj_rest_auth.registration.urls')
    ),
    path(
        'api/rest-auth/password/reset/confirm/<uidb64>/<token>/',
        PasswordResetConfirmView.as_view(),
        name='password_reset_confirm',
    ),
]
