from django.contrib import admin

from app_kochbuch.models.favourite import Favourite


@admin.register(Favourite)
class AdminFavourite(admin.ModelAdmin):
    list_display = ('recipe', 'user')
    search_fields = ('recipe__name', 'user__username')