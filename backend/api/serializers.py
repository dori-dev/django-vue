from django.contrib.auth import get_user_model
from rest_framework import serializers

from blog import models

User = get_user_model()


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Article
        fields = [
            'id',
            'title',
            'slug',
            'author',
            'content',
            'status',
            'published',
        ]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
