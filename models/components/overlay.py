############################################################
############################################################

##     model name: Overlay                    
##     superclass: Flex
##     subclass:   
##     points to: Container, Section, Link 
##     abstract: No

##     description:
"""
it is used to create an overlay, an element that is over 
another. it can have images as bg and contains a link to somewhere
it always span the entire dimension of the containers or
the sections it points to
it has no margin but it can have a padding
the position is fixed to be absolute and al, the params
like top start bottom end are set to zero
the container or section overlayed has to be relative positioned
overlay is a flex container
"""

##     parameters:
#           +CSS
#           +Flex 
#           container
#           section
#           name
#           

##       methods:
#           __str__
#         

####    Admin stuff

##    fixed CSS-Flex parameters:
#            width
#            height
#            col
#            position
#            top start botton end
#            display
#           

##    ignored in admin param:
#           margin
#           breakpoint
#           

############################################################
############################################################

from django.db import models
from ..abstract.abstract import Flex

from ..layout.container import Container, Section
from ..content.link import Link
from .button import Button

class Overlay(Flex):
    name = models.CharField(
        max_length=10,
        blank=True,
    )
    #where you can apply an overlay:
    containers = models.ManyToManyField(
        Container,
        blank=True,
        )
    sections = models.ManyToManyField(
        Section,
        blank=True,
        )
    #what you can put inside:
    link = models.ForeignKey(
        Link,
        blank=True, 
        null=True,
        on_delete=models.SET_NULL,
        )
    button = models.ForeignKey(
        Button,
        blank=True, 
        null=True,
        on_delete=models.SET_NULL,
        )

    #if not visible, increase this value
    level = models.IntegerField(
        blank=True,
        null=True,
        default=5000,
        )

    def __str__(self):
        return 'Overlay ' + self.name

        