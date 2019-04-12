from django.db import models
from rest_framework.compat import MinValueValidator

from app_kochbuch.models.recipe import Recipe
from app_kochbuch.models.unit import Unit


class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe, related_name='ingredient_recipe', on_delete=models.CASCADE)
    number = models.FloatField(
        default = 0,
        validators = [MinValueValidator(0), ]
    )
    unit = models.ForeignKey(Unit, related_name='ingredient_unit', on_delete=models.PROTECT)
    ingredient = models.CharField(max_length=100)
    comment = models.CharField(max_length=300, blank=True)