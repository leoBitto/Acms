############################################################
############################################################

##     model name: section                    
##     superclass: Flex
##     subclass:   
##     points to: Page
##     abstract: No

##     description:
#           the section display a series of container 
#           organizing them in a row. if the section dont have
#           a value for the height parameter it adapts to the
#           content, if it is set to 100 it span the entire
#           height OF THE VIEWPORT.
#           the break point parameter allow you to set a 
#           media query to organize the content in a column
#           a section always span the entire width of the 
#           viewport

##     parameters:
#           +CSS
#           +Flex 
#           name
#           page
#
##       methods:
#           __str__

####    Admin stuff

##    fixed CSS-Flex parameters:
#           sizes:
#               width
#           misc:
#               display
#           flex_properties:
#               flex-flow

##    ignored in admin param:
#           position
#           sizes


############################################################
############################################################
from django.db import models

from ..abstract.abstract import Flex
from ..pages import Page

class Section(Flex):
    #every section group the containers, 
    name = models.CharField(max_length=100, null=True)
    page = models.ForeignKey(
        Page,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        )
    
    
    def __str__(self):
        return self.name  
