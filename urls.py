from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('index', views.base, name='index'),
    path('page', views.base, name='page'),
    path('landing', views.base),
]