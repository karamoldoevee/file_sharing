from django.contrib import admin
from webapp.models import File


class FileAdmin(admin.ModelAdmin):
    list_display = ['pk', 'signature', 'upload', 'author', 'created_at', 'status']
    list_filter = ['status']
    list_display_links = ['pk', 'signature']
    search_fields = ['signature']
    fields = ['signature', 'upload', 'author', 'status']
    readonly_fields = ['created_at']


admin.site.register(File, FileAdmin)
