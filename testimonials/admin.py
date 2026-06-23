from django.contrib import admin
from .models import Testimonial


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'rating', 'is_active', 'display_order')
    list_editable = ('rating', 'is_active', 'display_order')
    search_fields = ('name', 'role', 'message')
