from django.db import models

from ..abstract.abstract import Flex
from ..pages import Page
from ..content.image import Image
from ..content.text import Text

class Section(Flex):
    #every section group the containers, 
    #the sections can be ordered

    name = models.CharField(max_length=100, null=True)
    page = models.ManyToManyField(Page)
    
    
    def __str__(self):
        return self.name  


class Container(Flex):
    name = models.CharField(
        null=True, 
        blank=True, 
        max_length=100,
        )
    section = models.ManyToManyField(
        Section, 
        )
    texts = models.ManyToManyField(
        Text,
        blank=True, 
        )
    images = models.ManyToManyField(
        Image,
        blank=True, 
        )

    @property
    def orderedContent(self):
        ordered = []
        #recall all txt linked
        for t in self.texts.all():
            ordered.append(t)
        #recall all image linked
        for i in self.images.all():
            ordered.append(i)
        # order them by .order
        ordered.sort(key=lambda x: x.order)
        #return list if there are items
        #else if empty return false
        if len(ordered)==0:
            return False 
        return ordered

    class Meta:
        ordering=['order']

    def __str__(self):
        return 'Container' + self.name


