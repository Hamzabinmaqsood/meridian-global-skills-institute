from django.contrib import admin
from .models import FAQ


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'is_active', 'display_order')
    list_editable = ('is_active', 'display_order')
    search_fields = ('question', 'answer')
