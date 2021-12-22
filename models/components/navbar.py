
from django.db import models
from ..abstract.abstract import Flex

class Navbar(Flex):
    width = 100
    margin = '-0'
    ##logo
    #optional image inside the navbar-brand
    #div
    logo = models.ImageField(upload_to='', null=True, blank=True)
    ##nome brand
    #it refer to the element with the class
    #'navbar-brand'
    brand_name = models.CharField(
            max_length=25,
            blank=True,
            null=True,
            help_text="this is the name of the brand"
        )

    ##color
    navbar_color = models.CharField(
            choices=[
                ('navbar-dark','dark'),
                ('navbar-light','light'),
            ],
            max_length = 25,
            blank=True,
            null=True,
            help_text="""
            this is the color of the navbar, the object
            accept also the bg colors of css
            this helps you create contrast between the 
            bg color and the text
            """
        ) 
    ##position(placement)
    position = models.CharField(
                    choices=[
                            ('', 'default position'),
                            ('fixed-top', 'fixed top'),
                            ('fixed-bottom', 'fixed bottom'),
                            ('sticky-top', 'sticky top'),
                            
                            ],
                                blank=True,
                                null=True, 
                                max_length=20
                            )
    
    def __str__(self):
        return "navbar"
