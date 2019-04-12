from asyncio.test_utils import mock_nonblocking_socket

from django.db import models
from django.contrib.auth.models import User
from rest_framework.compat import MinValueValidator

from app_kochbuch.models.severity import Severity


class Recipe(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField(
        default = 1,
        validators = [MinValueValidator(1),]
    )
    working_time_min = models.IntegerField(default=0)
    cooking_time_min = models.IntegerField(default=0)
    repose_time_min = models.IntegerField(default=0)
    description = models.CharField(max_length=2500)
    severity = models.ForeignKey(Severity, related_name='recipe_severity', on_delete=models.PROTECT)
    user = models.ForeignKey(User, related_name='recipe_user', on_delete=models.CASCADE)
    date = models.DateField(help_text='YYYY-MM-DD')
    image = models.ImageField(upload_to='recipe_image', blank=True)

    def __str__(self):
        return self.name
