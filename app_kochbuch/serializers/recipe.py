from django.db.models import Avg
from rest_framework import serializers

from app_kochbuch.models.rating import Rating
from app_kochbuch.models.recipe import Recipe
from app_kochbuch.serializers.severity import SeveritySerializer


class RecipeSerializer(serializers.ModelSerializer):
    severity = SeveritySerializer(read_only=True)
    average = serializers.SerializerMethodField(read_only=True)

    severity_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Recipe
        fields = ('id', 'name', 'quantity', 'working_time_min', 'cooking_time_min', 'repose_time_min', 'date', 'image'
                  , 'severity', 'user'
                  , 'average'
                  , 'severity_id')

    def get_average(self, obj):
        return Rating.objects.filter(recipe=obj).aggregate(rating=Avg('rating'))['rating'] or 0