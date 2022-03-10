#from django.conf.urls import url
from turtle import pos
from django.db import models
from django.db.models.signals import post_save, post_delete

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

        

def post_page_created_signal(sender, instance, created, **kwargs):    
    print(sender, instance.name, created)
    from ..urls import urlpatterns
    from ..views import views
    from django.urls import path
    #add the name and the url to urlpatterns
    if instance.url == '':
        n = instance.name
    else:
        n = instance.url
    urlpatterns.append(
            path(
                instance.url, 
                views.base, 
                name=n
                )
            )
    print("done!")
    print(urlpatterns)


def post_page_deleted_signal(sender, instance, **kwargs):
    print(sender, instance)
    from ..urls import urlpatterns
    from django.urls import path
    from ..views import views
    pages = Page.objects.all()
    for page in pages:
        if page.url == '':
            n = page.name
        else:
            n = page.url
        urlpatterns.append(
                path(
                    page.url, 
                    views.base, 
                    name=n
                    )
                )
    print("fixed!")
    print(urlpatterns)

post_save.connect(post_page_created_signal, sender=Page)
post_delete.connect(post_page_deleted_signal, sender=Page)