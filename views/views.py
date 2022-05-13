from django.shortcuts import get_object_or_404, render

from ..models.pages import Page

from ..models.components.navbar import Navbar

from django.contrib.auth.models import User

# Create your views here.
def base(request):
    path = request.path[1:]
    page = get_object_or_404(Page, url = path)
    
    context = {
        'page'  : page,        
        }

    return render(request, 'base.html', context)


def firstLanding(request):
    return render(request, 'firstLanding.html', {})

