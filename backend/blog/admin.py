from django.contrib import admin
from blog import models


@admin.register(models.Article)
class BlogAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'author',
        'updated',
        'status',
    ]
    list_filter = [
        'status',
    ]
    search_fields = [
        'title',
        'content',
        'author__username',
        'slug',
    ]
    date_hierarchy = 'created'
    raw_id_fields = [
        'author',
    ]
