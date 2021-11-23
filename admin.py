from django.contrib import admin
from django.utils.html import format_html

from .models.pages import PageIndex
from .models.blocks import BlockSection

# Register your models here.
class PageAdmin(admin.ModelAdmin):
    list_display = ()


class BlockSectionAdmin(admin.ModelAdmin):
    list_display = ()

admin.site.register(PageIndex, PageAdmin)
admin.site.register(BlockSection, BlockSectionAdmin)