
from django.db import models
from ..abstract.abstract import Flex
from ..content.image import Image

"""
Navbar component model it is rendered with a <nav>
one navbar can be pointed by the Nav elements that allow to choose which

"""

class Navbar(Flex):


    has_user_functionality = models.BooleanField(default=False)

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
    #it refer to the <a> element with the class
    #'navbar-brand'
    brand_name = models.CharField(
            max_length=25,
            blank=True,
            null=True,
            default='',
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
    def get_links(self):
        links=[]
        for nav in self.nav_set.all():
            if nav.url_toPage == '' : 
                u=nav.name
            else: 
                u=nav.url_toPage
            links.append((nav.name, u))#'Acms:' + 
        return links

    def __str__(self):
        return "navbar"


class Nav(models.Model):
    name = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        help_text='the string shown in the navbar'
    )
    url_toPage = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        help_text="""the url that the page has
            it must contain a namespace from the url
            its not a page to avoid circular import"""
    )
    navbar = models.ForeignKey(
        Navbar,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        help_text='the navbar the nav belongs to'
    )
    order = models.IntegerField(
        help_text='the order the nav has'
    )

    disabled = models.CharField(
        max_length=20,
        null=True,
        blank=True,
        choices=[
            ('disabled', 'disabled'),
            ('','active'),
            ],
        default='',
        help_text='if disabled the link is shown as greyish'
    )
