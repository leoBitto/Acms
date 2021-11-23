from django.shortcuts import render
from .models.pages import Page
from django.conf import settings

# Create your views here.
def index(request):
    page = Page.objects.get(url = 'index')
    print("page", page.url)
    sections = page.get_sections.all()
    print("sections", sections)
    sections_list = []
    for section in range(0, len(sections)):
        sections_list.append(sections[section].text_set.all())
    print("content", sections_list)
    context = {
        'sections': sections,
        'section_list' : sections_list,
    }
    return render(request, 'index.html', context)