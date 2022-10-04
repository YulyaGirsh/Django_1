from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


class EventsAdmin(admin.ModelAdmin):
    list_display = ['title', 'time_create', 'cat', 'get_html_photo', 'is_published']
    list_display_links = ['title', 'cat']
    search_fields = ['title', 'content']
    list_editable = ['is_published']
    list_filter = ['title', 'time_create', 'cat', 'is_published']
    prepopulated_fields = {'slug': ('title',)}
    fields = ('title', 'slug','cat', 'photo', 'get_html_photo', 'is_published', 'time_create')
    readonly_fields = ('time_create', 'get_html_photo')

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}'width =50>")

    get_html_photo.short_description = 'Фото'


class AreaAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Events, EventsAdmin)
admin.site.register(Area, AreaAdmin)

admin.site.site_title = 'Админ-панель 1'
admin.site.site_header = 'Админ-панель 2'
