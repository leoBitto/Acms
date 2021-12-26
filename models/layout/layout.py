from django.db import models
from ..pages import Page
from ..abstract.abstract import Flex

class Section(Flex):
    #every section group the containers, 
    #the sections can be ordered

    name = models.CharField(max_length=100, null=True)
    page = models.ForeignKey(Page, on_delete=models.SET_NULL, blank=True, null=True)
    
    
    def __str__(self):
        return "Section " + self.order[-1] + " of " + str(self.page.name)  


class Container(Flex):
    name = models.CharField(
        null=True, 
        blank=True, 
        max_length=100,
        )
    section = models.ForeignKey(
        Section, 
        on_delete=models.SET_NULL, 
        blank=True, 
        null=True,
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


