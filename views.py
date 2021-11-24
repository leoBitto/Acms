
from django.shortcuts import render
from .models.pages import Page
from .models.blocks import BlockNav
from django.conf import settings

# Create your views here.
def base(request):
    path = request.path[1:]
    page = Page.objects.get(url = path)
    print("page", page)
    sections = page.blocksection_set.all()
    sections_list = []
    for s in sections:

        section = {
            'text': s.text_set.all(),
            'flex_mode' : s.flex_RC,
            'name':s.name,
            'position': s.position,
            'width': s.width,
            'height': s.height,
        }
        sections_list.append(section)
    

    context = {
        'height' : page.height,
        'width'  : page.width,
        'has_navbar' : page.has_navBar,
        'section_list' : sections_list,
    }
    if page.has_navBar:
        pages = BlockNav.objects.all()[0].get_pages
        print('pages', pages)
        context['navbar'] = pages
    print(context['navbar'])
    return render(request, 'section.html', context)