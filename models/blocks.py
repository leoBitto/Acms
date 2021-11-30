from django.db import models
from django.db.models.base import Model
from django.db.models.fields import CharField
from .abstract import BlockGraphic
from .pages import Page

class BlockSection(BlockGraphic):
    name = models.CharField(max_length=100, blank=True, null=True)
    position = models.IntegerField(default=1, null=True, blank=True)
  
    page = models.ForeignKey(Page, on_delete=models.SET_NULL, blank=True, null=True)


    def __str__(self):
        return 'Section ' + str(self.name)



class BlockLink(BlockGraphic):
    name = CharField(max_length= 50, default='',blank=True,null=True)
    pointing_to = CharField(max_length=50, 
                    default='',
                    blank=True,
                    
                    )
    rendered_in= CharField(max_length=50, 
                    default='',
                    blank=True,
                    
                    )
    
    def __str__(self):
        return 'Link ' + str(self.name)



class BlockContent(BlockGraphic):
    name = models.CharField(max_length=100, blank=True, null=True)
    position = models.IntegerField(default=1, null=True, blank=True)

    has_link = models.BooleanField(null=True, blank=True, default=False)
    link = models.ForeignKey(BlockLink, on_delete=models.SET_NULL, blank=True, null=True)

    section = models.ForeignKey(BlockSection, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return  str(self.name)



class BlockNav(BlockGraphic):
    name = models.CharField(
            blank=True,
            default="navbar",
            null=True,
            max_length=50,
                )    

    @property
    def get_pages(self):
        pages = Page.objects.all()
        lst=[]
        for p in pages:
            lst.append(p)
        return lst



    def __str__(self):
        return self.name


