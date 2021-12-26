from django.db import models
from ..layout.layout import Container
from ..abstract.abstract import CSS

class Image(CSS):

    #content 
    url = models.ImageField(upload_to='', null=True, blank=True)
    #meta about the content
    author = models.CharField(max_length=100, null=True, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    container = models.ForeignKey(Container, on_delete=models.SET_NULL, null=True, blank=True)
    #col = models.ForeignKey(Col, on_delete=models.SET_NULL, null=True, blank=True)


    def __str__(self):
        return str(self.url)