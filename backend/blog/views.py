from django.views import generic

from blog import models


class ArticleList(generic.ListView):
    def get_queryset(self):
        return models.Article.objects.filter(status="P")
