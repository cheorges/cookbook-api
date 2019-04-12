from django.db.models import Avg
from rest_framework import serializers

from app_kochbuch.models.rating import Rating
from app_kochbuch.models.recipe import Recipe
from app_kochbuch.models.recipecategory import RecipeCategory
from app_kochbuch.serializers.ingredient import IngredientDetailSerializer
from app_kochbuch.serializers.rating import RatingSerializer
from app_kochbuch.serializers.recipecategory import RCCategoryDetailSerializer
from app_kochbuch.serializers.severity import SeveritySerializer
from app_kochbuch.serializers.user import UserSerializer


class RecipeDetailSerializer(serializers.ModelSerializer):
    ingredient_recipe = IngredientDetailSerializer(read_only=True, many=True)
    severity = SeveritySerializer(read_only=True)
    user = UserSerializer(read_only=True)
    average = serializers.SerializerMethodField(read_only=True)
    recipecategory_category = serializers.SerializerMethodField(read_only=True)

    severity_id = serializers.IntegerField(write_only=True)
    user_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Recipe
        fields = ('id', 'name', 'quantity', 'working_time_min', 'cooking_time_min', 'repose_time_min', 'description', 'date', 'image'
            , 'ingredient_recipe', 'severity', 'user'
            , 'recipecategory_category'
            , 'average'
            , 'severity_id', 'user_id')

    def get_average(self, obj):
        return Rating.objects.filter(recipe=obj).aggregate(rating=Avg('rating'))['rating'] or 0

    def get_recipecategory_category(self, obj):
        recipe_category = RecipeCategory.objects.filter(recipe=obj)
        return [RCCategoryDetailSerializer(c).data for c in recipe_category]