from django.db import models
from ..abstract.abstract import CSS
from ..layout.layout import Container


class Text(CSS):

    #content 
    txt = models.TextField(null=True, blank=True)
    #meta about the content
    author = models.CharField(max_length=100, null=True, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    container = models.ForeignKey(Container, on_delete=models.SET_NULL, null=True, blank=True)
    #col = models.ForeignKey(Col, on_delete=models.SET_NULL, null=True, blank=True)

    #to implement:
    #text color from utilities in bootstrap docs
    #OVERFLOW FROM UTILITIES
    #vertical align
    #text from utils


    def __str__(self):
        return self.txt