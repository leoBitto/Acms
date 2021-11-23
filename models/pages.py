from django.db import models
from django.db.models.base import Model

# Create your models here.
class Page(models.Model):
    #this is the page model, it should gather
    #all the sections associated with it ;
    #also the css properties that shoulb 
    #be passed to the template should be here
    width = models.IntegerField(null=True, blank=True, default=100)

    url = models.CharField(null=True, max_length=100)
    @property
    def get_sections(self):
        return self.blocksection_set.all() 

    