from django.db import models
from django.db.models.base import Model
from .pages import PageIndex

class BlockSection(models.Model):
    content = models.CharField(max_length=100, blank=True, null=True)
    page = models.ForeignKey(PageIndex, on_delete=models.CASCADE, blank=True, null=True)