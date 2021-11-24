from django.contrib import admin
from django.utils.html import format_html

from .models.pages import Page
from .models.blocks import BlockSection, BlockNav
from .models.content import Text

# Register your models here.
class PageAdmin(admin.ModelAdmin):
    list_display = ('url', 'width', 'height', 'flex_RC', 'has_navBar',)


class BlockSectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'width', 'height', 'flex_RC', 'page')


class BlockNavAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'get_pages',)


class TextsAdmin(admin.ModelAdmin):
    list_display = ('txt', 'author', 'creation_date', 'width', 'height', 'section')

admin.site.register(Page, PageAdmin)
admin.site.register(BlockSection, BlockSectionAdmin)
admin.site.register(BlockNav, BlockNavAdmin)
admin.site.register(Text, TextsAdmin)
