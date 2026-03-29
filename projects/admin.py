from django.contrib import admin
from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'featured', 'created_at')
    search_fields = ('title', 'description')
    list_filter = ('featured', 'created_at')
    prepopulated_fields = {'slug': ('title',)}
