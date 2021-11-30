from django.shortcuts import render
from ..models.pages import Page
from ..models.blocks import BlockLink, BlockNav
from django.conf import settings

# Create your views here.
def base(request):
    path = request.path[1:]
    page = Page.objects.get(url = path)
    
    sections = page.blocksection_set.all()
    sections_list = []
    for s in sections:
        contents = s.blockcontent_set.all()
        
        content_list = []
        for content in contents:
            
            texts_list = []
            for text in content.text_set.all():
                texts_list.append(text)
                
            images_list = []
            for image in content.image_set.all():
                images_list.append(image)

            packed_content = {
                'position' : content.position,
                'has_link' : content.has_link,
                'width'    : content.width,
                'height'   : content.height,
                'flex_mode': content.flex_RC,
                'flex_grow': content.flex_grow,
                'padding'  : content.padding,
                'margin'   : content.margin,
                'texts'    : texts_list,
                'images'   : images_list
                            }
            if content.has_link:
                link = BlockLink.objects.get(rendered_in = content.name)
                print(link)
                packed_content['link'] = link
            
            content_list.append(packed_content)

        section = {
            'content_list': content_list,
            'flex_mode'   : s.flex_RC,
            'flex_grow'   : s.flex_grow,
            'name'        : s.name,
            'position'    : s.position,
            'width'       : s.width,
            'height'      : s.height,
            'padding'     : s.padding,
            'margin'      : s.margin,
        }
        # print(section)
        sections_list.append(section)
    

    context = {
        'page_height' : page.height,
        'page_width'  : page.width,
        'page_flex'   : page.flex_RC,
        'has_navbar'  : page.has_navBar,
        'section_list': sections_list,
    }
    if page.has_navBar:
        navbar = BlockNav.objects.all()[0]
        context['navbar'] = navbar
    print(context)
    return render(request, 'section.html', context)