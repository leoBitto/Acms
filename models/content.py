from django.db import models

from .blocks import BlockSection

class Text(models.Model):

    #content 
    txt = models.TextField(null=True, blank=True)
    #meta about the content
    author = models.CharField(max_length=100, null=True, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    #css properties of the content
    width = models.IntegerField(null=True, blank=True, default=100)
    height = models.IntegerField(null=True, blank=True, default=100)

    section = models.ForeignKey(BlockSection, on_delete=models.SET_NULL, null=True, blank=True)


    def __str__(self):
        return self.txt
