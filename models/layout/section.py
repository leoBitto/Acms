from turtle import width
from django.db import models

from ..abstract.abstract import Flex
from ..pages import Page

class Section(Flex):
    #every section group the containers, 
    
    width=100

    name = models.CharField(max_length=100, null=True)
    page = models.ForeignKey(
        Page,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        )
    
    
    def __str__(self):
        return self.name  
