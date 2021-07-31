from django.contrib import admin
from .models import Directory,DirectoryItem


class DirectoryItemAdmin(admin.ModelAdmin):
    list_display = ('element_code','value','parent')
    list_display_links=('element_code','value')
    search_fields = ('code','value')

admin.site.register(Directory)
admin.site.register(DirectoryItem,DirectoryItemAdmin)
