from django.contrib import admin
from django.utils.html import format_html

from .models.pages import Page
from .models.content.image import Image
from .models.content.text import Text
from .models.layout.layout import *
from .models.components.link import Link
from .models.components.navbar import Navbar
from .models.components.overlay import Overlay


class PageAdmin(admin.ModelAdmin):
    list_display = ( 
        'name',
        'url', 
        'navbar',
        )
    list_filter = (
        'name',
        )
    search_fields = (
        'name',
        )
    fieldsets = (
        ('Urls and Meta',
            {
                'fields': (
                    'url',
                    'name',
                    'title',
                    'description',
                    ),
                'description': """title and description refer 
                                to the metadata of the HTML page
                                url is what is seen in the address bar
                                the name is used for organization
                                purpose inside the site administration""",
            }
            ),
        ('Components',
            {
                'fields':('has_footer','navbar',),
                'description':"""indicate the two (or three, modals 
                                should be added ) components that 
                                can be inserted in a page"""
            }
        )
        )
    

class SectionAdmin(admin.ModelAdmin):
    list_display = (
                    'name',
                    'page',
                    'order',
        )
    fieldsets = (
        ('Section Properties',
            {
                'fields':('name','page',),
                'description':"""the properties relative to the section"""
            }
        ),
        ('CSS property',
            {
                'fields': (
                        ('CSS_id','CSS_classes',),
                        ('width','height',),
                        ('padding','padding_sides',),
                        ('margin','margin_sides',),
                        'breakpoint',
                        ('bg_image',
                        'bg_color',
                        'bg_gradient',
                        'shadow',),
                        'position',
                        ('top',
                        'left',
                        'down',
                        'right',),
                        'order',
                        'visibility',
                        'display',
                        ),
                'description': """these properties set the classes
                                that bootstrap use""",
                'classes':('collapse',),
            }
            ),
        ('Flex property',
            {
                'fields': ('direction',
                        'justify_content',
                        'align_items',
                        'align_self',
                        'align_content',
                        'flex_grow',
                        ),
                'description': """these properties set the classes
                                that bootstrap use to manage flexbox""",
                'classes':('collapse',),
            }
            ),

        )
    list_filter = (
        'name',
        'page',
        )


class NavbarAdmin(admin.ModelAdmin):
    list_display = (
            '__str__',
            'logo',
            'brand_name',
            'navbar_color',
            'placement',
        )
    fieldsets = (
        ('Navbar Properties',
            {
                'fields':(
                    'logo',
                    'brand_name',
                    'navbar_color',
                    'placement',
                    ),
                'description':"""the properties relative to the navbar"""
            }
        ),
        ('CSS property',
            {
                'fields': (
                        'breakpoint',
                        'bg_color',
                        'bg_gradient',
                        ),
                'description': """these properties set the classes
                                that bootstrap use""",
                'classes':('collapse',),
            }
            ),
        ('Flex property',
            {
                'fields': (
                        
                        'justify_content',
                        
                        ),
                'description': """these properties set the classes
                                that bootstrap use to manage flexbox""",
                'classes':('collapse',),
            }
            ),

        )
  

class ContainerAdmin(admin.ModelAdmin):
    list_display = (
                    'name',
                    'section',
                    'order',
        )
    fieldsets = (
        ('Container Properties',
            {
                'fields':('name','section','order',),
                'description':"""the properties relative to the container"""
            }
        ),
               ('CSS property',
            {
                'fields': (
                        ('CSS_id','CSS_classes',),
                        ('width','height',),
                        ('padding','padding_sides',),
                        ('margin','margin_sides',),
                        'breakpoint',
                        ('bg_image',
                        'bg_color',
                        'bg_gradient',
                        'shadow',),
                        'position',
                        ('top',
                        'left',
                        'down',
                        'right',),
                        'visibility',
                        'display',
                        ),
                'description': """these properties set the classes
                                that bootstrap use""",
                'classes':('collapse',),
            }
            ),
        ('Flex property',
            {
                'fields': ('direction',
                        'justify_content',
                        'align_items',
                        'align_self',
                        'align_content',
                        'flex_grow',
                        ),
                'description': """these properties set the classes
                                that bootstrap use to manage flexbox""",
                'classes':('collapse',),
            }
            ),

        )
    list_filter = (
        'name',
        'section',
       
        )
    

class OverlayAdmin(admin.ModelAdmin):
    list_display = (
            #should be added a bg
            'container',
            'section',
        )
    fieldsets = (
        ('Overlay Properties',
            {
                'fields':('container', 'section',),
                'description':"""the properties relative to the Overlay"""
            }
            ),
        ('CSS property',
            {
                'fields': (
                        ('CSS_id','CSS_classes',),
                        'breakpoint',
                        'position',
                        ('bg_image',
                        'bg_color',
                        'bg_gradient',
                        'shadow',),
                        'visibility',
                        'display',
                        ),
                'description': """these properties set the classes
                                that bootstrap use""",
                'classes':('collapse',),
            }
            ),
        ('Flex property',
            {
                'fields': ('direction',
                        'justify_content',
                        'align_items',
                        'align_self',
                        'align_content',
                        'flex_grow',
                        ),
                'description': """these properties set the classes
                                that bootstrap use to manage flexbox""",
                'classes':('collapse',),
            }
            ),
        )
    list_filter = (
        'container',
        
        )


class LinkAdmin(admin.ModelAdmin):
    list_display = (
        'getLink',
        'toPage',
        'textShown',
     )
    fieldsets = (
        ('Link Properties',
            {
                'fields':(  'toPage',
                            'textShown',
                            'container', 
                            'overlay',
                            'stretched_link',
                            ),
                'description':"""the properties relative to the Link"""
            }
            ),
        ('CSS property',
            {
                'fields': (
                        ('CSS_id','CSS_classes',),
                        'breakpoint',
                        ('bg_image',
                        'bg_color',
                        'bg_gradient',
                        'shadow',),
                        'position',
                        ('top',
                        'left',
                        'down',
                        'right',),
                        'order',
                        'visibility',
                        'display',
                        ),
                'description': """these properties set the classes
                                that bootstrap use""",
                'classes':('collapse',),
            }
            ),
        ('Flex property',
            {
                'fields': ('direction',
                        'justify_content',
                        'align_items',
                        'align_self',
                        'align_content',
                        'flex_grow',
                        ),
                'description': """these properties set the classes
                                that bootstrap use to manage flexbox""",
                'classes':('collapse',),
            }
            ),
        )


class TextAdmin(admin.ModelAdmin):
    list_display = (
                    'txt', 
                    'author', 
                    'creation_date', 
                    
                    'container',
                    )
    fieldsets = (
        ('Text Properties',
            {
                'fields':('txt', 
                        'author',
                        'container',
                        'color',
                        'overflow',
                        'alignment',
                        'size',
                        'weight',
                        'italics',
                        'line_height',
                        'text_decoration',
                        'vertical_align',
                        ),
                'description':"""the properties relative to the Text css"""
            }
            ),
        ('CSS property',
            {
                'fields': (
                        ('CSS_id','CSS_classes',),
                        ('width','height',),
                        ('padding','padding_sides',),
                        ('margin','margin_sides',),
                        'breakpoint',
                        ('bg_image',
                        'bg_color',
                        'bg_gradient',
                        'shadow',),
                        'position',
                        ('top',
                        'left',
                        'down',
                        'right',),
                        'order',
                        'visibility',
                        'display',
                        ),
                'description': """these properties set the classes
                                that bootstrap use""",
                'classes':('collapse',),
            }
            ),
        )
 

class ImageAdmin(admin.ModelAdmin):
    list_display = (
                    'id', 
                    'url', 
                    'author', 
                    'creation_date', 
                     
                    'container',
                    'image_tag',
                    )
    fieldsets = (
        ('Overlay Properties',
            {
                'fields':('url', 'author','container'),
                'description':"""the properties relative to the Image css"""
            }
            ),
        ('CSS property',
            {
                'fields': (
                        ('CSS_id','CSS_classes',),
                        ('width','height',),
                        ('padding','padding_sides',),
                        ('margin','margin_sides',),
                        'breakpoint',
                        ('bg_image',
                        'bg_color',
                        'bg_gradient',
                        'shadow',),
                        'position',
                        ('top',
                        'left',
                        'down',
                        'right',),
                        'order',
                        'visibility',
                        'display',
                        ),
                'description': """these properties set the classes
                                that bootstrap use""",
                'classes':('collapse',),
            }
            ),
        )

    def image_tag(self,obj):
        return format_html('<img src="{0}" style="height:200px;" />'.format(obj.url.url))


admin.site.register(Page, PageAdmin)
admin.site.register(Navbar, NavbarAdmin)
admin.site.register(Text, TextAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(Container, ContainerAdmin)
admin.site.register(Overlay, OverlayAdmin)
admin.site.register(Link,LinkAdmin)
admin.site.register(Image, ImageAdmin)

