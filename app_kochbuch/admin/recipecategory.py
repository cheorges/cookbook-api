from django.contrib import admin

from app_kochbuch.models.recipecategory import RecipeCategory


@admin.register(RecipeCategory)
class AdminRecipeCategory(admin.ModelAdmin):
    list_display = ('recipe', 'category')
    search_fields = ('recipe__name', 'category__name')
    list_filter = ('category',)