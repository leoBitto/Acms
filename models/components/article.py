############################################################
############################################################

##     model name: Article                    
##     superclass: Models
##     subclass:   
##     points to: Container
##     abstract: No

##     description: 
"""
it contains an article, a series of images and text. 
it is an extension of the base.html
it refer to a general topic so it can be filtered.
"""

##     parameters:
#           author
#           date_created
#           date_updated
#           url 
#           title
#           paragraphs         

##       methods:
#           __str__
#           orderedContent

####    Admin stuff

##    fixed CSS-Flex parameters:


##    ignored in admin param:


############################################################
############################################################
from ..layout.container import Container
from django.db import models


class Article(models.Model):

    # Meta
    author = models.CharField(
        max_length=10,
        blank=True,
        null=True,
    )
    date_created = models.DateTimeField(
        auto_now_add=True, 
        editable=False,
        )
    date_updated = models.DateTimeField(
        auto_now=True,
        )
    topic = models.CharField(
        max_length=15,
        blank=True,
        null=True,
    )
    # every page is pointed by an url that must be set 
    # in the url patterns when the object is saved
    # the url setted is:
    slug = models.SlugField(
        max_length=100,
        blank=True,
        null=True,
    )
    title = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )
    paragraphs = models.ManyToManyField(
        Container,
    )
        

