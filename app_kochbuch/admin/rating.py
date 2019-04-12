from django.contrib import admin

from app_kochbuch.models.rating import Rating


@admin.register(Rating)
class AdminRating(admin.ModelAdmin):
    list_display = ('rating', 'title', 'date', 'user', 'recipe')
    list_filter = ('rating',)
    search_fields = ('recipe__name', 'user__username')