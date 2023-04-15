from django.urls import path
from api import views

app_name = 'api'
urlpatterns = [
    path('', views.ArticleList.as_view(), name='list'),
    path('users/', views.UserList.as_view(), name='users'),
    path('<slug:slug>/', views.ArticleDetail.as_view(), name='detail'),
    path('user/<slug:username>/', views.UserDetail.as_view(), name='user'),
]
