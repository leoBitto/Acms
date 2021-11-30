from django.db import models
from .abstract import BlockGraphic
from .blocks import BlockContent

class Text(BlockGraphic):

    #content 
    txt = models.TextField(null=True, blank=True)
    #meta about the content
    author = models.CharField(max_length=100, null=True, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    

    block = models.ForeignKey(BlockContent, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.txt


class Image(BlockGraphic):

    #content 
    url = models.ImageField(upload_to='', null=True, blank=True)
    #meta about the content
    author = models.CharField(max_length=100, null=True, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    
    block = models.ForeignKey(BlockContent, on_delete=models.SET_NULL, null=True, blank=True)


    def __str__(self):
        return str(self.url)
