from django.contrib import admin

from .models import Video, Stranic

class VideoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('title',)

class StranicAdmin(admin.ModelAdmin):
    list_display = ('id', 'str_title')
    list_display_links = ('str_title',)

admin.site.register(Stranic, StranicAdmin)
admin.site.register(Video, VideoAdmin)