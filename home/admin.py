from django.contrib import admin
from .models import Song, SortFilter, God

class SongAdmin(admin.ModelAdmin):
    list_display = ('name', 'sort_filter', 'Raga')


admin.site.register(Song, SongAdmin)

class SortFilterAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


admin.site.register(SortFilter, SortFilterAdmin)

class GodAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

admin.site.register(God, GodAdmin)