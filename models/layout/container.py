from django.db import models

from ..abstract.abstract import Flex
from ..layout.section import Section
from ..content.image import Image
from ..content.text import Text
from ..content.link import Link
"""
Container have .content inside, they are the most generic 
grouping object. 
they belong to only one section and this is because otherwise
the orderparameter cant be used to organize the containers 
inside a section. 

it can point to many types of content with ManyToMany like :
    .text
    .images
    .links, the cover the entire container making it cliccable
pointing to the section is done with ForeignKey 

"""
class Container(Flex):

    name = models.CharField(
        null=True, 
        blank=True, 
        max_length=100,
        )
    section = models.ForeignKey(
        Section,
        blank=True,
        null=True,
        on_delete=models.SET_NULL, 
        )
    texts = models.ManyToManyField(
        Text,
        blank=True, 
        )
    images = models.ManyToManyField(
        Image,
        blank=True, 
        )
    link = models.ForeignKey(
        Link,
        blank=True, 
        null=True,
        on_delete=models.SET_NULL,
        )
    col= models.CharField(null=True, 
        blank=True, 
        max_length=100,)

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
        return 'Container ' + self.name


