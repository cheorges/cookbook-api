from django.contrib import admin

from app_kochbuch.models.category import Category


@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ('name', 'comment')
    search_fields = ('name',)