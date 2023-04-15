from django.contrib.auth import get_user_model
from rest_framework import generics

from blog import models
from api import serializers

User = get_user_model()


class ArticleList(generics.ListCreateAPIView):
    queryset = models.Article.objects.all()
    serializer_class = serializers.ArticleSerializer


class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Article.objects.all()
    serializer_class = serializers.ArticleSerializer
    lookup_field = "slug"


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    lookup_field = "username"
