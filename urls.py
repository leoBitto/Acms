from django.conf import settings
from django.urls import path
from .views import views
#from django.conf.urls.static import static

app_name = 'Acms'
urlpatterns = [
    path('articles/<slug:slug>', views.articleView, name='article'),
]

# # add this lines
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

