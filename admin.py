from django.contrib import admin
from django.utils.html import format_html

from .models.pages import Page
from .models.blocks import BlockSection
from .models.content import Text

# Register your models here.
class PageAdmin(admin.ModelAdmin):
    list_display = ('url', 'width')


class BlockSectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'position',)


class TextsAdmin(admin.ModelAdmin):
    ...

admin.site.register(Page, PageAdmin)
admin.site.register(BlockSection, BlockSectionAdmin)
admin.site.register(Text, TextsAdmin)