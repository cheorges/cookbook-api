from rest_framework import serializers

from app_kochbuch.models.favourite import Favourite
from app_kochbuch.serializers.recipe import RecipeSerializer


class FavouriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favourite
        fields = '__all__'

class FavouriteDetailSerializer(serializers.ModelSerializer):
    recipe = RecipeSerializer(read_only=True)

    recipe_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Favourite
        fields = ('id', 'user', 'recipe', 'recipe_id')