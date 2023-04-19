from django.urls import path
from api import views

app_name = 'api'
urlpatterns = [
    path('articles/', views.ArticleList.as_view(), name='list'),
    path('article/<slug:slug>/', views.ArticleDetail.as_view(), name='detail'),
    path('author/<int:pk>/', views.AuthorDetail.as_view(), name='author'),
    path('users/', views.UserList.as_view(), name='users'),
    path('user/<slug:username>/', views.UserDetail.as_view(), name='user'),
]
