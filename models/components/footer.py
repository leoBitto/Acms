from django.db import models
from ..abstract.abstract import Flex

class Footer(Flex):

    #content 
    logo = models.ImageField(upload_to='', null=True, blank=True)
    text_l = models.TextField(null=True, blank=True, default='')
    text_r = models.TextField(null=True, blank=True, default='')

    def __str__(self):
        return 'footer'