from django.contrib import admin
from .models import *

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'parent', 'slug', 'template', 'is_active', 'created', 'updated')
    list_filter = ('template', 'is_active', 'created', 'updated')
    list_per_page = 10
    search_fields = ('title',)
    view_on_site = True

admin.site.register(Page, PageAdmin)
