from django.contrib import admin
from .models import Directory,DirectoryItem


class DirectoryItemAdmin(admin.ModelAdmin):
    list_display = ('element_code','value','parent')
    list_display_links=('element_code','value')
    search_fields = ('code','value')


class DirectoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'version', 'start_date')
    list_display_links = ('name', 'version', 'start_date')
    search_fields = ('name', 'version', 'start_date')


admin.site.register(Directory)
admin.site.register(DirectoryItem,DirectoryItemAdmin)
