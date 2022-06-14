############################################################
############################################################

##     model name: Grid                    
##     superclass: Flex
##     subclass:   
##     points to: Section, container
##     abstract: No

##     description:
"""
grid container

"""

##     parameters:
#           +CSS
#           +Flex 
#           name
#           section
#           container

##       methods:
#           __str__
#           orderedContent

####    Admin stuff

##    fixed CSS-Flex parameters:


##    ignored in admin param:



############################################################
############################################################

from django.db import models

from ..abstract.abstract import Flex
from ..layout.section import Section


class Grid(Flex):

    name = models.CharField(
        null=True, 
        blank=True, 
        max_length=100,
        )
    #where the grid is
    section = models.ForeignKey(
        Section,
        blank=True,
        null=True,
        on_delete=models.SET_NULL, 
        )
    
    # the grid parameters
    gap = models.CharField(
        max_length=10,
        null=True,
    )   
    cell_min = models.CharField(
        max_length=10,
        null = True,
    )
   

    def __str__(self):
        return 'grid ' + self.name


