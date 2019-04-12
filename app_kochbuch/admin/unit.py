from django.contrib import admin

from app_kochbuch.models.unit import Unit


@admin.register(Unit)
class AdminUnit(admin.ModelAdmin):
    list_display = ('abstract', 'unit', 'comment')
    search_fields = ('abstract', 'unit')