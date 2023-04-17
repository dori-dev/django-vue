from django.contrib.auth import get_user_model
from rest_framework import generics
from blog import models
from api import serializers, permissions

User = get_user_model()


class ArticleList(generics.ListCreateAPIView):
    queryset = models.Article.objects.all()
    serializer_class = serializers.ArticleSerializer


class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Article.objects.all()
    serializer_class = serializers.ArticleSerializer
    lookup_field = "slug"
    permission_classes = [
        permissions.IsAuthorOrReadOnly |
        permissions.IsSuperUser
    ]


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [
        permissions.IsSuperUser |
        permissions.IsStaffReadOnly
    ]


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    lookup_field = "username"
    permission_classes = [
        permissions.IsSuperUser |
        permissions.IsItSelf |
        permissions.IsStaffReadOnly
    ]
