from django.db import models

from ..content.text import Text
from ..content.image import Image
from ..abstract.abstract import Flex

class Footer(Flex):


    logo = models.ForeignKey(
        Image,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        )
    text_l = models.ManyToManyField(
        Text,
        related_name='left_text',
        )
    text_r = models.ManyToManyField(
        Text,
        related_name='right_text',
        )

    def __str__(self):
        return 'footer'