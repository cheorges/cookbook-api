from django.contrib.auth.models import User
from django.db import models

from app_kochbuch.models.recipe import Recipe


class Favourite(models.Model):
    user = models.ForeignKey(User, related_name='favourite_user', on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, related_name='favourite_recipe', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'recipe')