from django.contrib import admin
from .models import *
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'intro', 'is_publish', 'created', 'updated')
    list_per_page = 20
    search_fields = ['name', 'intro']
    list_filter = ('is_publish', 'created', 'updated')

admin.site.register(Page, PageAdmin)
