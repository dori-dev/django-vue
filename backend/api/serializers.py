from rest_framework import serializers
from blog import models


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
