from django.contrib.auth import get_user_model
from rest_framework import serializers

from blog import models

User = get_user_model()


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
        ]


class ArticleSerializer(serializers.ModelSerializer):
    # author = serializers.HyperlinkedIdentityField(view_name='api:author')
    # author = serializers.CharField(
    #     source='author.username',
    #     read_only=True,
    # )
    author = serializers.SerializerMethodField('get_author')

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

    def get_author(self, obj):
        return obj.author.username

    def validate_title(self, value):
        blocked_list = [
            'php',
            'laravel',
            'java',
        ]
        for word in blocked_list:
            if word.lower() in value:
                raise serializers.ValidationError(
                    f'You are not allowed to use the name {word}'
                )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
