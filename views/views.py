from django.shortcuts import get_object_or_404, render
from django.http import Http404
from ..models.pages import Page
from django.conf import settings

# Create your views here.
def base(request):
    path = request.path[1:]
    page = get_object_or_404(Page, url = path)

    context = {
        'page'     : page,
        #'rows_list': rows_list,
        
        }
    print(context['page'])
    print(page.url)
    from ..urls import urlpatterns
    print(urlpatterns)
    return render(request, 'base.html', context)