
from django.db import models
from ..abstract.abstract import Flex
from ..content.image import Image
"""
Navbar component model it is rendered with a <nav>
one navbar can be 
"""
class Navbar(Flex):

    ##logo
    #optional image inside the navbar-brand
    #div
    logo = models.ForeignKey(
        Image, 
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        )
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
    placement = models.CharField(
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
    
    @property
    def get_pages(self):
        from ..pages import Page
        links=[]
        for page in Page.objects.all():
            if page.url == '' : 
                u=page.name 
            else: u=page.url
            links.append((page.name, 'Acms:' + u))
        return links

    def __str__(self):
        return "navbar"
