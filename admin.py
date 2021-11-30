from django.contrib import admin
from django.utils.html import format_html

from .models.pages import Page
from .models.blocks import BlockSection, BlockNav, BlockContent, BlockLink
from .models.content import Image, Text

# Register your models here.
class PageAdmin(admin.ModelAdmin):
    list_display = ('name', 'url','has_navBar',
                    )


class BlockContentAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'section')


class BlockSectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'page')


class BlockNavAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'get_pages',)



class BlockLinkAdmin(admin.ModelAdmin):
    list_display = ('name' , 'pointing_to', 'rendered_in', 
                    )


class TextAdmin(admin.ModelAdmin):
    list_display = ('txt', 'author', 'creation_date', 
                     'block')


class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'url', 'author', 'creation_date', 
                    'block', 'image_tag',)

    def image_tag(self,obj):
        return format_html('<img src="{0}" style="height:200px;" />'.format(obj.url.url))


admin.site.register(Page, PageAdmin)
admin.site.register(BlockSection, BlockSectionAdmin)
admin.site.register(BlockNav, BlockNavAdmin)
admin.site.register(BlockLink, BlockLinkAdmin)
admin.site.register(Text, TextAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(BlockContent, BlockContentAdmin)
