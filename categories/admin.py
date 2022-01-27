from django.contrib import admin
from categories.models import Category

# Register your models here.
@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ['title', 'slug', 'published']