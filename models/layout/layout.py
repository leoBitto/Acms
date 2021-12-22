from django.db import models
from .. import pages
from ..abstract.abstract import Flex
from django.core.validators import MaxValueValidator, MinValueValidator


class Row(Flex):
    
    name = models.CharField(
        max_length=50, 
        blank=True
        )
    
    order = models.IntegerField()
    #dimension = models.PositiveIntegerField(default=10, validators=[MinValueValidator(1), MaxValueValidator(100)])

    #page = models.ForeignKey(pages.Page, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return ' Row ' + str(self.order)  
    

class Col(Flex):
    name = models.CharField(
        max_length=50, 
        blank=True
        )

    breakpoint = models.CharField(
        max_length=10,
        choices=[
            ('sm','-sm'),
            ('md','-md'),
            ('lg','-lg'),
            ('xl','-xl'),
            ('xxl','-xxl'),
            ('fluid','-fluid'),
        ],
        default='',
        blank=True,
        )

    align_self = models.CharField(
        max_length=10,
        choices=[
            ('start','-start'),
            ('center','-center'),
            ('end','-end'),
        ],
        default='',
        blank=True,
        )
    
    justify_content = models.CharField(
        max_length=10,
        choices=[
            ('start','-start'),
            ('center','-center'),
            ('end','-end'),
            ('around','-around'),
            ('between','-between'),
            ('evenly','-evenly'),
        ],
        default='',
        blank=True,
        )
    
    dimension = models.PositiveIntegerField(default='', validators=[MinValueValidator(1), MaxValueValidator(12)], blank=True, null=True)
    
    order = models.IntegerField()
    
    row = models.ForeignKey(Row, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return str(self.row) + ' Col ' + str(self.order)


class Grid(Flex):
    ...


class Container(Flex):
    name = models.CharField(
        null=True, 
        blank=True, 
        max_length=100,
        )
    section = models.ForeignKey(
        pages.Section, 
        on_delete=models.SET_NULL, 
        blank=True, 
        null=True,
        )
    col = models.ForeignKey(
        Col, 
        on_delete=models.SET_NULL, 
        blank=True, 
        null=True,
        )
    order = models.IntegerField(
        blank=True,
        null=True,
        default=1,
     )

    @property
    def orderedContent(self):
        ordered = []
        #recall all txt linked
        for t in self.text_set.all():
            ordered.append(t)
        #recall all image linked
        for i in self.image_set.all():
            ordered.append(i)
        # order them by .order
        ordered.sort(key=lambda x: x.order)
        #return list if there are items
        #else if empty return false
        if len(ordered)==0:
            return False 
        return ordered

    class Meta:
        ordering=['order']

    def __str__(self):
        return 'Container' + self.name
