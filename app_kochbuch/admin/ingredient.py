from django.contrib import admin

from app_kochbuch.models.ingredient import Ingredient


@admin.register(Ingredient)
class AdminIngredient(admin.ModelAdmin):
    list_display = ('number', 'unit', 'ingredient', 'comment', 'recipe')
    list_filter = ('unit__unit',)
    search_fields = ('recipe__name',)

    def unit(self, obj):
        return obj.unit.unit
    def ingredient(self, obj):
        return obj.ingredient.ingredient
    def recipe(self, obj):
        return obj.recipe.name