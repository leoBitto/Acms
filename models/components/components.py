from ..content.content import Text
from ..abstract.abstract import CSS, Flex
from django.db import models
from ..pages import Page
from ..layout.layout import Container

class Overlay(Flex):
    ## da mettere nei template
    width = 100
    height = 100
    padding = "-0"
    margin = "-0"
    position = "position-absolute"
    top = 0
    left = 0
    down = 0
    right = 0
    container = models.ForeignKey(
        Container,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        )
    
    def __str__(self):
        return 'Overlay ' + self.container.name

        

class Link(models.Model):
    toPage = models.ForeignKey(
        Page,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        )
    textShown = models.ForeignKey(
        Text,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        )
    container = models.ForeignKey(
        Container,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        )
    overlay = models.ForeignKey(
        Overlay,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        )


    @property
    def getLink(self):
        print(self.toPage.url)
        return 'Acms:' + self.toPage.url
         
        

    def __str__(self):
        return "Link to " + self.toPage.name