from django.db import models
from django.db.models.base import Model

# Create your models here.
class PageIndex(models.Model):
    @property
    def get_sections(self):
        return self.blocksection_set.all() 

    