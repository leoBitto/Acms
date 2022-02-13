#from django.conf.urls import url
from django.db import models

from .components.navbar import Navbar
from .components.footer import Footer

class Page(models.Model):
    #this is the page model, every page contains a certain number
    # of sections, every page CAN point to a navbar and a footer
    
    url = models.CharField(blank=True, max_length=100, unique=True)
    name = models.CharField(blank=True, null=True, default=url, max_length=100, unique=True)

    navbar = models.ForeignKey(
        Navbar,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        )

    footer = models.ForeignKey(
        Footer,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        )

    description = models.TextField(
        blank=True,
        null=True,
        )
    title = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.url

    def model_save(self, *args, **kwargs):
        from ..urls import urlpatterns
        from ..views import views
        from django.urls import path
        #add the name and the url to urlpatterns
        if self.url == '':
            n = self.name
        else:
            n = self.url
        urlpatterns.append(
                path(
                    self.url, 
                    views.base, 
                    name=n
                    )
                )
        #super().save(*args, **kwargs)#call the real save() method   

    def delete(self, *args, **kwargs):
        from ..urls import urlpatterns
       
        for l in urlpatterns:
            if l.name == self.url:
                urlpatterns.remove(l)
       
        super().delete(*args, **kwargs)#real delete()
        

    
