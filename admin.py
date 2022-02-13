from django.contrib import admin
from django.utils.html import format_html

from .models.pages import Page
from .models.content.image import Image
from .models.content.text import Text
from .models.layout.container import Container
from .models.layout.grid import Grid
from .models.layout.section import Section
from .models.content.link import Link
from .models.components.navbar import Navbar
from .models.components.footer import Footer
from .models.components.overlay import Overlay

html_tags =('HTML tags',
            {
            'fields': (
                    ('CSS_id','CSS_classes',),
                    ),
            'description': """these properties set the HTML tags""",
            'classes':('collapse',),
            })
sizes= ('Sizes',
            {
            'fields':(('height','width'), 'col'),
            'description':"sizes of the div, they refer to min viewports. leave height empty to make it adapt to content. the width is always set to 100",
            'classes':('collapse','wide'),
            })
spacing=('Spacing',
            {
            'fields':(
                    ('padding','padding_sides',),
                    ('margin','margin_sides',),
                    ),
            'description':"padding and margins",
            'classes':('collapse',),
            })
background=('Background',
            {
            'fields': (
                    'bg_image',
                    'bg_color',
                    'bg_gradient',
                    'shadow',
                    ),
            'description':"background properties",
            'classes':('collapse',),                        
            })
position=('Position',
            {
            'fields':(
                    'order',
                    'position',
                    ('top',
                    'left',
                    'down',
                    'right',),
                    ),
            'description':"positioning",
            'classes':('collapse',),
            })
misc=('Misc',
            {
            'fields':
                    ('breakpoint',
                    'visibility',
                    'opacity',
                    ('display',
                     'inline',),
                     ('borders', 'borders_colors')
                     ),
            'description':"miscellaneous properties, breakpoint refer to the flex direction",
            'classes':('collapse',),
            })
flex_properties=('Flex properties',
            {
            'fields': (
                    'direction',
                    'align_self',
                    'justify_content',
                    'align_items',
                    'align_content',
                    'flex_grow',
                    'flex_wrap',
                   
                    ),
            'description': """these properties set the classes
                            that bootstrap use to manage flexbox""",
            'classes':('collapse',),
            })

class PageAdmin(admin.ModelAdmin):
    list_display = ( 
        'name',
        'url', 
        'navbar',
        'footer',
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
                    'navbar',
                    'footer',
                    ),
                'description': """title and description refer 
                                to the metadata of the HTML page
                                url is what is seen in the address bar
                                the name is used for organization
                                purpose inside the site administration""",
            }
            ),
     
        )


class NavbarAdmin(admin.ModelAdmin):
    list_display = (
            '__str__',
            'brand_name',
            'navbar_color',
            'placement',
        )
    fieldsets = (
        ('Navbar Properties',
            {
                'fields':(
                    #'pages_with_navbar',
                    'logo',
                    'brand_name',
                    'navbar_color',
                    'placement',
                    'has_user_functionality',
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
  

class FooterAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',   
    )


class SectionAdmin(admin.ModelAdmin):
    list_display = (
                    'name',
                    'page',
                    'order',
        )
    fieldsets = (
            ('Section properties',
            {
                'fields':(
                    'name', 
                    'page',
                )
            }),
            html_tags,
            ('Sizes',
                {
                'fields':('height',),
                'description':" in this case it only accepts values from 0 to 100. height of the section, they refer to min viewports. leave height empty to make it adapt to content, make it 100 to make it span all the viewport. the width is always set to 100",
                'classes':('collapse','wide'),
                }),      
            spacing,
            background,
            ('Misc',
                {
                'fields':
                        ('breakpoint',
                        'visibility',
                        'inline',
                        ),
                'description':"breakpoint refer to the flex direction, display is flex. IS MANDATORY IF YOU SET DIRECTION ROW",
                'classes':('collapse',),
                }),
            flex_properties,
        )

    list_filter = (
        'name',
        'page',
        )


class GridAdmin(admin.ModelAdmin):
    list_display = (
                    'name',
                    'section',
                    'order',
        )
    fieldsets = (
            ('Grid Properties',
                {
                    'fields':(
                        'name',
                        'section',
                        'gap',
                        'cell_min',
                        ),
                    'description':"""the properties relative to the grid"""
                }),
            html_tags,
            sizes,
            spacing,
           
            misc,
            )

    list_filter = (
        'name',
        'section',
       
        )


class ContainerAdmin(admin.ModelAdmin):
    list_display = (
                    'name',
                    'section',
                    'grid',
                    'order',
        )
    fieldsets = (
            ('Container Properties',
                {
                    'fields':(
                        'name',
                        'section',
                        'grid',
                        'texts',
                        'images',
                        'link',
                        ),
                    'description':"""the properties relative to the container
                                        the sections it belongs to
                                        and the content it contain"""
                }),
            html_tags,
            sizes,
            background,
            spacing,
            position,
            misc,
            flex_properties
            )

    list_filter = (
        'name',
        'section',
       
        )
      

class ButtonAdmin(admin.ModelAdmin):
    list_display = (
                    'name',
                    'order',
        )
    fieldsets = (
            ('Button Properties',
                {
                    'fields':(
                        'name',
                       
                        ),
                    'description':"""the properties relative to the button"""
                }),
            html_tags,
            sizes,
            spacing,
            background,
            position,
            misc,
            flex_properties,
            )

    list_filter = (
        'name',       
        )
    

class OverlayAdmin(admin.ModelAdmin):
    list_display = (
            #should be added a bg
           '__str__',
           'level',
        )
    fieldsets = (
        ('Overlay Properties',
            {
                'fields':('containers', 'sections', 'link', 'level'),
                'description':"""the properties relative to the Overlay"""
            }
            ),
        html_tags,
       ('Spacing',
            {
            'fields':(
                    ('padding','padding_sides',),
                    ),
            'description':"padding and margins",
            'classes':('collapse',),
            }),
        background,
        ('Misc',
            {
            'fields':
                    (
                    'visibility',
                    'opacity',
                    'inline',
                     ),
            'description':"miscellaneous properties, breakpoint refer to the flex direction",
            'classes':('collapse',),
            }),
        flex_properties,
        )
    list_filter = (
        'containers',
        'sections',
        )


class LinkAdmin(admin.ModelAdmin):
    list_display = (
        'getLink',
        'toPage',
        'external_link',
        'textShown',
     )
    fieldsets = (
        ('Link Properties',
            {
                'fields':(  'toPage',
                            'external_link',
                            'textShown',
                            'stretched_link',
                            ),
                'description':"""the properties relative to the Link"""
            }
            ),
        ('HTML tags',
                {
                'fields': (
                        ('CSS_id','CSS_classes',),
                        ),
                'description': """these properties set the HTML tags""",
                'classes':('collapse',),
                }
        ),
        ('Background',
            {
            'fields': (
                    'bg_image',
                    'bg_color',
                    'bg_gradient',
                    'shadow',
                    ),
            'description':"background properties",
            'classes':('collapse',),                        
            }),
        ('Position',
            {
            'fields':(
                    'order',
                    'position',
                    ('top',
                    'left',
                    'down',
                    'right',),
                    ),
            'description':"positioning",
            'classes':('collapse',),
            }),
        ('Misc',
            {
            'fields':
                    ('breakpoint',
                    'visibility',
                    ('display',
                    'inline',),
                    ),
            'description':"miscellaneous properties, breakpoint refer to the flex direction",
            'classes':('collapse',),
            }),
        ('Flex properties',
            {
            'fields': (
                    'direction',
                    'align_self',
                    'justify_content',
                    'align_items',
                    'align_content',
                    'flex_grow',
                    'flex_wrap',
                
                    ),
            'description': """these properties set the classes
                            that bootstrap use to manage flexbox""",
            'classes':('collapse',),
            }),
        
        )


class TextAdmin(admin.ModelAdmin):
    list_display = (
                    '__str__', 
                    'author', 
                    'creation_date', 
                    )
    fieldsets = (
        ('Text Properties',
            {
                'fields':('txt', 
                        'author',
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
                    #'url', 
                    'author', 
                    'creation_date', 
                    'image_tag',
                    )
    
    #add_form_template = 'admin/image_form.html'
    #change_form_template = 'admin/image_form.html'

    fieldsets = (
        ('Image Properties',
            {
                'fields':(
                    'url',
                    'author',
               
                    ),
                'description':"""the properties relative to the Image css"""
            }
            ),
        html_tags,
        sizes,
        ('Default image',
            {
                'fields': (
                    ('bg_image','bg_color','bg_gradient','shadow',),
                    ('visibility',),
                    'object_fit',
                    ('borders', 'borders_colors'),
                    ),
                'description':""" the default image or color that the img tag
                                refer to when the resource cant be found and other things
                                """,
                'classes':('collapse',),
            }
            ),
        )


    def image_tag(self,obj):
        return format_html('<img src="{0}" style="height:400px;" />'.format(obj.url.url))


admin.site.register(Page, PageAdmin)
admin.site.register(Navbar, NavbarAdmin)
admin.site.register(Grid, GridAdmin)
admin.site.register(Footer, FooterAdmin)
admin.site.register(Text, TextAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(Container, ContainerAdmin)
admin.site.register(Overlay, OverlayAdmin)
admin.site.register(Link,LinkAdmin)
admin.site.register(Image, ImageAdmin)


