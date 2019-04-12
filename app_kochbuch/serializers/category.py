from rest_framework import serializers

from app_kochbuch.models.category import Category
from app_kochbuch.models.recipecategory import RecipeCategory


class CategorySerializer(serializers.ModelSerializer):
    amount = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Category
        fields = ('id', 'name', 'comment', 'amount')

    def get_amount(self, obj):
        return RecipeCategory.objects.filter(category=obj).count()