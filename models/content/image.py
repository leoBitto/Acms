from django.db import models
from ..abstract.abstract import CSS

class Image(CSS):

    #set CSS parameters
    display = '-block'

    #content 
    url = models.ImageField(upload_to='', null=True, blank=True)
    #meta about the content
    author = models.CharField(max_length=100, null=True, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return str(self.url)