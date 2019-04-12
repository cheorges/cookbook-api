from django.contrib import admin
from django.db.models import Avg
from rest_framework import serializers

from app_kochbuch.models.favourite import Favourite
from app_kochbuch.models.ingredient import Ingredient
from app_kochbuch.models.rating import Rating
from app_kochbuch.models.recipe import Recipe
from app_kochbuch.models.recipecategory import RecipeCategory


class IngredientInline(admin.TabularInline):
    model = Ingredient
    extra = 0


class RecipeCategoryInline(admin.TabularInline):
    model = RecipeCategory
    extra = 0


class FavouriteInline(admin.TabularInline):
    model = Favourite
    extra = 0


class RatingInline(admin.TabularInline):
    model = Rating
    extra = 0


@admin.register(Recipe)
class AdminRecipe(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'severity', 'date', 'user', 'average')
    readonly_fields = ('average',)
    search_fields = ('name',)
    list_filter = ('severity',)
    inlines = [IngredientInline, RatingInline, RecipeCategoryInline,FavouriteInline]

    def average(self, obj):
        return Rating.objects.filter(recipe=obj).aggregate(rating=Avg('rating'))['rating'] or 0