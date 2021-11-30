from django.db import models
from .abstract import BlockGraphic 

# Create your models here.
class Page(BlockGraphic):
    #this is the page model, it should gather
    #all the sections associated with it ;
    #also the css properties that shoulb 
    #be passed to the template should be here
    #width = models.IntegerField(null=True, blank=True, default=100)
    #height = models.IntegerField(null=True, blank=True, default=100)
    #flex_RC = models.CharField(choices=[('row', 'row'),('column','column')], blank=True, null=True, max_length=20)
    url = models.CharField(blank=True, max_length=100, )
    name = models.CharField(blank=True, default=url, max_length=100)
    has_navBar = models.BooleanField(null=True, blank=True, default=False)


    def __str__(self):
        return self.name

    