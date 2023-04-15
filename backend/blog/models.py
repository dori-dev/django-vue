from django.db import models
from django.contrib.auth import get_user_model
from django.utils.timezone import now

UserModel = get_user_model()


class Article(models.Model):
    STATUS_CHOICES = (
        ('D', 'Draft'),
        ('P', 'Published'),
    )
    title = models.CharField(
        max_length=255,
    )
    slug = models.SlugField(
        max_length=8,
        unique=True,
    )
    author = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        related_name='articles',
    )
    content = models.TextField()
    published = models.DateTimeField(
        default=now,
    )
    created = models.DateTimeField(
        auto_now_add=True,
    )
    updated = models.DateTimeField(
        auto_now=True,
    )
    status = models.CharField(
        max_length=1,
        choices=STATUS_CHOICES,
        default='D',
    )

    def save(self, *args, **kwargs) -> None:
        self.title = self.title.title()
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.title
