from django.contrib import admin
from .models import GalleryImage


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'display_order', 'created_at')
    list_editable = ('is_active', 'display_order')
    search_fields = ('title', 'description')
    list_filter = ('is_active', 'created_at')
