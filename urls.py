from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import views

urlpatterns = [
    path('base', views.base, name='base'),
    path('page', views.base, name='page'),
    path('test', views.base, name='test'),
    path('', views.base, name='index'),
    path('landing', views.base),
]

# add this lines
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)