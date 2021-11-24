from django.db import models
from django.db.models.base import Model
from .pages import Page

class BlockSection(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    position = models.IntegerField(default=1, null=True, blank=True)
    
    width = models.IntegerField(null=True, blank=True, default=100)
    height = models.IntegerField(null=True, blank=True, default=100)
    flex_RC = models.CharField(choices=[('row', 'row'),('column','column')], blank=True, null=True, max_length=20)

    
    page = models.ForeignKey(Page, on_delete=models.SET_NULL, blank=True, null=True)

    @property
    def get_content(self):
        return self.text_set.all()

    def __str__(self):
        return 'Section ' + str(self.position)



class BlockNav(models.Model):
    name = models.CharField(
            blank=True,
            default="navbar",
            null=True,
            max_length=50,
                )
    position = models.CharField(choices=[
            ('leftSide','leftSide'),
            ('rightSide','rightSide'),
            ('top','top'),
            ('down','down'),
            ],
        max_length=50,
        blank=True, 
        null=True,
        default="top"
        )
    

    @property
    def get_pages(self):
        pages = Page.objects.all()
        lst=[]
        for p in pages:
            lst.append(p.url)
        return lst



    def __str__(self):
        return self.name


    