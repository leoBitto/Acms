############################################################
############################################################

##     model name: Card                    
##     superclass: Flex
##     subclass:   
##     points to: Grid, Text,Image,Link
##     abstract: No

##     description:
"""
Card are similar to container but they are used to dispose 
content inside a grid

it can point to many types of content with ManyToMany like :
    .text, various text can be aggregated in a container. 
            useful for articles
    .images, its advised to use only one image per container
            the container should be dedicated to that image only
    .links, the cover the entire container making it cliccable
pointing to the section is done with ForeignKey 

IMages can be added also as backgrounds

to add:

header and footer
title
descri

"""

##     parameters:
#           +CSS
#           +Flex 
#           name
#           section
#           texts
#           images
#           link
#           

##       methods:
#           __str__
#           orderedContent

####    Admin stuff

##    fixed CSS-Flex parameters:


##    ignored in admin param:



############################################################
############################################################
from django.db import models
from django.db import models

from ..abstract.abstract import Flex
from ..layout.section import Section
from ..layout.grid import Grid
from ..content.image import Image
from ..content.text import Text
from ..content.link import Link

class Card(Flex):

    name = models.CharField(
        null=True, 
        blank=True, 
        max_length=100,
        )
    # where a container can be
    section = models.ForeignKey(
        Section,
        blank=True,
        null=True,
        on_delete=models.SET_NULL, 
        )
    grid = models.ForeignKey(
        Grid,
        blank=True,
        null=True,
        on_delete=models.SET_NULL, 
        )
    # thing card can contain
    
    text = models.ForeignKey(
        Text,
        blank=True, 
        null=True,
        on_delete=models.SET_NULL, 
        )
    
    image = models.ForeignKey(
        Image,
        blank=True, 
        null=True,
        on_delete=models.SET_NULL, 
        )

    link = models.ForeignKey(
        Link,
        blank=True, 
        null=True,
        on_delete=models.SET_NULL,
        )

    class Meta:
        ordering=['order']

    def __str__(self):
        return 'Card ' + self.name


