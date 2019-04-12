from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    comment = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return '%s' % (self.name)