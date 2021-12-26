from django.db import models
from ..abstract.abstract import Flex

from ..layout.layout import Container, Section

class Overlay(Flex):
    ## da mettere nei template
    width = 100
    height = 100
    padding = "-0"
    margin = "-0"
    # position = "position-absolute"
    # top = 0
    # left = 0
    # down = 0
    # right = 0
    container = models.ForeignKey(
        Container,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        )
    section = models.ForeignKey(
        Section,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        )


    def __str__(self):
        return 'Overlay ' + self.container.name

        