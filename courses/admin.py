from django.contrib import admin
from .models import CourseCategory, Course


@admin.register(CourseCategory)
class CourseCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'category',
        'duration',
        'fee',
        'level',
        'is_featured',
        'is_active',
        'display_order',
    )
    list_filter = ('category', 'level', 'is_featured', 'is_active')
    search_fields = ('title', 'short_description', 'description')
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ('is_featured', 'is_active', 'display_order')
