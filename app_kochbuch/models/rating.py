from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from app_kochbuch.models.recipe import Recipe


class Rating(models.Model):
    rating = models.IntegerField(
        default = 1,
        validators = [MaxValueValidator(5), MinValueValidator(1)]
    )
    date = models.DateField(help_text='YYYY-MM-DD')
    title = models.CharField(max_length=200)
    comment = models.CharField(max_length=1000)
    recipe = models.ForeignKey(Recipe, related_name='rating_recipe', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='rating_user', on_delete=models.CASCADE)