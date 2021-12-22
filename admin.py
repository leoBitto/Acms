from django.contrib import admin
from django.utils.html import format_html

from .models.pages import Page, Section
from .models.content.content import Image, Text
from .models.layout.layout import *
from .models.components.components import *
from .models.components.navbar import Navbar


class PageAdmin(admin.ModelAdmin):
    list_display = ( 
        'name',
        'url', 
            )
    fieldsets = (
        ('Urls and Meta',
            {
                'fields': ('url','name','title','description',),
                'description': """title and description refer 
                                to the metadata of the HTML page""",
            }
            ),
        ('Components',
            {
                'fields':('has_footer',),
                'description':"""indicate the two (or three, modals 
                                should be added ) components that 
                                can be inserted in a page"""
            }
        )
        )
    list_filter = (
        'name',
        'title',
        )


class NavbarAdmin(admin.ModelAdmin):
    ...


class SectionAdmin(admin.ModelAdmin):
    list_display = (
                    'name',
                    'page',
                    'order',
        )
    fieldsets = (
        ('Section Properties',
            {
                'fields':('name','page','order'),
                'description':"""the properties relative to the section"""
            }
        ),
        ('CSS property',
            {
                'fields': ('width',
                        'height',
                        'padding',
                        'margin',
                        'breakpoint',
                        'bg_color',
                        'bg_gradient',
                        'position',
                        'top',
                        'left',
                        'down',
                        'right',
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


class ContainerAdmin(admin.ModelAdmin):
    list_display = (
                    'name',
                    'section',
                    'col',
                    'order',
        )
    fieldsets = (
        ('Container Properties',
            {
                'fields':('name','section','col','order',),
                'description':"""the properties relative to the container"""
            }
        ),
        ('CSS properties',
            {
                'fields': ('width',
                        'height',
                        'padding',
                        'margin',
                        'breakpoint',
                        'bg_color',
                        'bg_gradient',
                        'position',
                        'top',
                        'left',
                        'down',
                        'right',
                        'display',
                        ),
                'description': """these properties set the classes
                                that bootstrap use""",
                'classes':('collapse',),
            }
            ),
        ('Flex properties',
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
        'col',
        )


class OverlayAdmin(admin.ModelAdmin):
    list_display = (
            #should be added a bg
            'container',
        )
    fieldsets = (
        ('Overlay Properties',
            {
                'fields':('container',),
                'description':"""the properties relative to the Overlay"""
            }
            ),
        ('CSS properties',
            {
                'fields': (
                        'bg_color',
                        'bg_gradient',
                        ),
                'description': """these properties set the classes
                                that bootstrap use""",
                'classes':('collapse',),
            }
            ),
        
        ('Flex properties',
            {
                'fields': (
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
    )


class TextAdmin(admin.ModelAdmin):
    list_display = (
                    'txt', 
                    'author', 
                    'creation_date', 
                    'col', 
                    'container',
                    )
 

class ImageAdmin(admin.ModelAdmin):
    list_display = (
                    'id', 
                    'url', 
                    'author', 
                    'creation_date', 
                    'col', 
                    'container',
                    'image_tag',
                    )

    def image_tag(self,obj):
        return format_html('<img src="{0}" style="height:200px;" />'.format(obj.url.url))


class RowAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name_', 'order', 

                    )

    def name_(self,obj):
        return 'Row ' + obj.name


class ColAdmin(admin.ModelAdmin):
    list_display = ('name' , 'row')

    def render(self,obj):
        return format_html("")


admin.site.register(Page, PageAdmin)
admin.site.register(Navbar, NavbarAdmin)
admin.site.register(Text, TextAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(Container, ContainerAdmin)
admin.site.register(Overlay, OverlayAdmin)
admin.site.register(Link,LinkAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Row, RowAdmin)
admin.site.register(Col, ColAdmin)
