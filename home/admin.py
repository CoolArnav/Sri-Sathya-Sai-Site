from django.contrib import admin
from .models import Song, SortFilter

class SongAdmin(admin.ModelAdmin):
    list_display = ('name', 'sort_filter')


admin.site.register(Song, SongAdmin)

class SortFilterAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


admin.site.register(SortFilter, SortFilterAdmin)
