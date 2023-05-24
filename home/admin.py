from django.contrib import admin
from .models import Song, SortFilter, God, Raaga

class SongAdmin(admin.ModelAdmin):
    list_display = ('name', 'sort_filter')


admin.site.register(Song, SongAdmin)

class SortFilterAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


admin.site.register(SortFilter, SortFilterAdmin)

class GodAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

admin.site.register(God, GodAdmin)


class RaagaAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

admin.site.register(Raaga, RaagaAdmin)