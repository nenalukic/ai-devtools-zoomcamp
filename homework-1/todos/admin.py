from django.contrib import admin
from .models import Todo


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    """Admin interface for Todo model"""
    
    list_display = ['title', 'user', 'is_completed', 'due_date', 'created_at']
    list_filter = ['is_completed', 'created_at', 'due_date']
    search_fields = ['title', 'description']
    readonly_fields = ['created_at', 'updated_at']
    fieldsets = (
        ('Task Information', {
            'fields': ('title', 'description', 'user')
        }),
        ('Status & Dates', {
            'fields': ('is_completed', 'due_date', 'created_at', 'updated_at')
        }),
    )
