from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from app_kochbuch.models.ingredient import Ingredient
from app_kochbuch.serializers.ingredient import IngredientSerializer, IngredientDetailSerializer


class ViewIngredient(viewsets.ModelViewSet):
    serializer_class = IngredientSerializer
    queryset = Ingredient.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('recipe',)

    def get_serializer_class(self):
        if self.detail or self.request.GET.get('recipe', 0):
            return IngredientDetailSerializer
        return IngredientSerializer