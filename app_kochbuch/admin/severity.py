from django.contrib import admin

from app_kochbuch.models.severity import Severity


@admin.register(Severity)
class AdminSeverity(admin.ModelAdmin):
    list_display = ('name', 'comment')
    search_fields = ('name',)