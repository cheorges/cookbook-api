from rest_framework import serializers

from app_kochbuch.models.ingredient import Ingredient
from app_kochbuch.models.recipe import Recipe
from app_kochbuch.serializers.recipe import RecipeSerializer
from app_kochbuch.serializers.unit import UnitSerializer


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'


class IngredientDetailSerializer(serializers.ModelSerializer):
    unit = UnitSerializer(read_only=True)

    unit_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Ingredient
        fields = ('id', 'number', 'ingredient', 'comment', 'recipe', 'unit', 'unit_id')