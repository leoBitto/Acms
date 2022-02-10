from django.db import models

from ..abstract.abstract import CSS, Flex
from ..pages import Page
from .text import Text

class Link(Flex):
    width = 100
    height = 100
    padding = "-0"
    margin = "-0"
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

    stretched_link = models.CharField(
        choices=[
            ('','not stretched'),
            ('stretched-link','stretched'),
        ],
        max_length=15,
        blank=True,
        null=True,
        )

    @property
    def getLink(self):
        return 'Acms:' + self.toPage.name

    def __str__(self):
        return "Link to " + self.toPage.name