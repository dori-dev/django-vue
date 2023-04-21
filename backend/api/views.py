from django.contrib.auth import get_user_model
from rest_framework import generics

from blog import models
from api import serializers, permissions

User = get_user_model()


class ArticleList(generics.ListCreateAPIView):
    queryset = models.Article.objects.all()
    serializer_class = serializers.ArticleSerializer
    ordering = [
        '-published',
    ]
    filterset_fields = [
        "status",
        "author",
        "author__username",
    ]
    search_fields = [
        "title",
        "content",
        "author__username",
        "author__first_name",
        "author__last_name",
    ]
    ordering_fields = [
        "published",
        "title",
        "status",
    ]


class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Article.objects.all()
    serializer_class = serializers.ArticleSerializer
    lookup_field = "slug"
    permission_classes = [
        permissions.IsAuthorOrReadOnly |
        permissions.IsSuperUser
    ]


class AuthorDetail(generics.RetrieveAPIView):
    queryset = User.objects.filter(is_staff=True)
    serializer_class = serializers.AuthorSerializer


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.MyUserSerializer
    permission_classes = [
        permissions.IsSuperUser |
        permissions.IsStaffReadOnly
    ]


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.MyUserSerializer
    lookup_field = "username"
    permission_classes = [
        permissions.IsSuperUser |
        permissions.IsItSelf |
        permissions.IsStaffReadOnly
    ]
