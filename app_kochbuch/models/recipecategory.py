from django.db import models

from app_kochbuch.models.category import Category
from app_kochbuch.models.recipe import Recipe


class RecipeCategory(models.Model):
    recipe = models.ForeignKey(Recipe, related_name='recipecategory_recipe', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='recipecategory_category', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('recipe', 'category')