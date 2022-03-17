from django.shortcuts import get_object_or_404, render

from ..models.components.article import Article
from ..models.pages import Page
from django.views.generic.list import ListView


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


def firstLanding(request):
    return render(request, 'firstLanding.html', {})

class articleListView(ListView):
    model = Article
    pagination = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
        

def articleView(request, slug):
    
    article = get_object_or_404(Article, slug = slug)    
    context = {
        'article'  : article,        
        }

    return render(request, 'article.html', context)