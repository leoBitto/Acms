from django.shortcuts import get_object_or_404, render
from ..models.pages import Page


# Create your views here.
def base(request):
    path = request.path[1:]
    page = get_object_or_404(Page, url = path)

    context = {
        'page'  : page,        
        }

   

    # from ..urls import urlpatterns
    # print(urlpatterns)

    return render(request, 'base.html', context)