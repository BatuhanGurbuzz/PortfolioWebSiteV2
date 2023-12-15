from django.contrib import admin
from .models import Projects, Category, Tag
# Register your models here.

@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ("name",)

    search_fields = ('name',)

    prepopulated_fields = { 
        'slug':('name',) 
    }

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)

    search_fields = ('name',)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass