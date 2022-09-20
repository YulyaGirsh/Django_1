from django.contrib import admin

from .models import *


class EventsAdmin(admin.ModelAdmin):
    list_display = ['title', 'time_create', 'cat', 'is_published']
    list_display_links = ['title', 'cat']
    search_fields = ['title', 'content']
    list_editable = ['is_published']
    list_filter = ['title', 'time_create', 'cat', 'is_published']
    prepopulated_fields = {'slug': ('title',)}


class AreaAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Events, EventsAdmin)
admin.site.register(Area, AreaAdmin)
