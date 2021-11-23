from django.shortcuts import render
from .models.pages import PageIndex
from django.conf import settings

# Create your views here.
def index(request):
    page = PageIndex.objects.all()
    context = {
        'page':page[0],
    }
    return render(request, 'index.html', context)