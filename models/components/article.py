from django.db import models
from ..content.text import Text


class Article(models.Model):

    author = models.CharField(
        max_length=10,
        blank=True,
        null=True,
    )
    date_created = models.DateTimeField()
    paragraphs = models.ManyToManyField(
        Text,
    )
