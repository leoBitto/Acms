from django.db import models

from .blocks import BlockSection

class Text(models.Model):
    #content 
    txt = models.TextField(null=True, blank=True)
    #meta about the content
    author = models.CharField(max_length=100, null=True, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    section = models.ForeignKey(BlockSection, on_delete=models.SET_NULL, null=True, blank=True)

    #css properties of the content