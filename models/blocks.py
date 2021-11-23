from django.db import models
from django.db.models.base import Model
from .pages import Page

class BlockSection(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    position = models.IntegerField(default=1, null=True, blank=True)
    page = models.ForeignKey(Page, on_delete=models.CASCADE, blank=True, null=True)

    @property
    def get_content(self):
        return self.text

    