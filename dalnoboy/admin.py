from django.contrib import admin

from .models import Video

class VideoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('title',)

admin.site.register(Video, VideoAdmin)