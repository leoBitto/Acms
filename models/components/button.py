############################################################
############################################################

##     model name: Button                    
##     superclass: CSS
##     subclass:   
##     points to: 
##     abstract: No

##     description:
"""
this component is pointed by graphical components such as
overlays and container, **navbar** etc 
it allows to perform an action 
"""

##     parameters:
#           +CSS
#           name
#           action

##       methods:
#           __str__
#         

####    Admin stuff

##    fixed CSS-Flex parameters:
#           
#           

##    ignored in admin param:
#           

############################################################
############################################################

from django.db import models
from ..abstract.abstract import CSS

class Button(CSS):
    name = models.CharField(
        max_length=10,
        blank=True,
    )
    inside_text = models.CharField(
        max_length=100,
        blank=True,
    )

    def __str__(self):
        return 'Overlay ' + self.name

