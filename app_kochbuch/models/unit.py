from django.db import models

class Unit(models.Model):
    abstract = models.CharField(max_length=20)
    unit = models.CharField(max_length=100)
    comment = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return '%s [%s]' % (self.unit, self.abstract)