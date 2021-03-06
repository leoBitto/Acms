from django.apps import AppConfig

class AcmsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Acms'

    #ready method override
    def ready(self, *args, **kwargs):
        from .urls import urlpatterns
        from django.urls import path
        from .views import views
        #add the urls of the Page objects
        #in the db in urlpatterns in urls.py
        from .models.pages import Page

        try:
            pages = Page.objects.all()
            if not pages:
                urlpatterns.append(
                            path(
                                '', 
                                views.firstLanding, 
                                name="landing"
                                )
                            )
            else:
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
                super().ready(*args, **kwargs)
        except:
            super().ready(*args, **kwargs)
        
        