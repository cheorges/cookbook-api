from rest_framework import serializers


from app_kochbuch.models.recipecategory import RecipeCategory
from app_kochbuch.serializers.category import CategorySerializer
from app_kochbuch.serializers.recipe import RecipeSerializer


class RecipeCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = RecipeCategory
        fields = '__all__'


class RCRecipeDetailSerializer(serializers.ModelSerializer):
    recipe = RecipeSerializer(read_only=True)

    class Meta:
        model = RecipeCategory
        fields = ('id', 'category', 'recipe')


class RCCategoryDetailSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = RecipeCategory
        fields = ('id', 'category')


class RCDetailSerializer(serializers.ModelSerializer):
    recipe = RecipeSerializer(read_only=True)
    category = CategorySerializer(read_only=True)

    recipe_id = serializers.IntegerField(write_only=True)
    category_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = RecipeCategory
        fields = ('id', 'category', 'recipe', 'recipe_id', 'category_id')
