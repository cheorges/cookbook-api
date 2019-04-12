from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters, status
from rest_framework.decorators import action
from rest_framework.response import Response

from app_kochbuch.models.favourite import Favourite
from app_kochbuch.models.recipe import Recipe
from app_kochbuch.models.recipecategory import RecipeCategory
from app_kochbuch.serializers.favourite import FavouriteSerializer
from app_kochbuch.serializers.ingredient import IngredientSerializer
from app_kochbuch.serializers.recipe import RecipeSerializer
from app_kochbuch.serializers.recipecategory import RecipeCategorySerializer
from app_kochbuch.serializers.recipedetail import RecipeDetailSerializer


class ViewRecipe(viewsets.ModelViewSet):
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()
    filter_backends = (DjangoFilterBackend, filters.SearchFilter,)
    filter_fields = ('user', )
    search_fields = ('name',)

    def get_serializer_class(self):
        if self.request.GET.get('user',0) or self.request.GET.get('name',0):
            return RecipeSerializer
        if self.detail:
            return RecipeDetailSerializer
        return RecipeSerializer

    @action(methods=['post'], detail=True)
    def add_ingredient(self, request, pk=None):
        ingredient = IngredientSerializer(data=request.data)
        ingredient.initial_data['recipe'] = pk
        if ingredient.is_valid():
            ingredient.save()
            return Response({'status': 'successful'}, status=status.HTTP_200_OK)
        else:
            return Response(ingredient.errors, status=status.HTTP_400_BAD_REQUEST)


    @action(methods=['post'], detail=True)
    def add_favourite(self, request, pk=None):
        favourite = FavouriteSerializer(data=request.data)
        favourite.initial_data['recipe'] = pk
        if favourite.is_valid():
            favourite.save()
            return Response({'status': 'successful'} ,status=status.HTTP_200_OK)
        else:
            return Response(favourite.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['post'], detail=True)
    def remove_favourite(self, request, pk=None):
        favourite = Favourite.objects.filter(recipe=pk, user=request.data['user'])
        try:
            favourite.delete()
            return Response({'status': 'successful'})
        except:
            return Response(favourite.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['post'], detail=True)
    def add_category(self, request, pk=None):
        category = RecipeCategorySerializer(data=request.data)
        category.initial_data['recipe'] = pk
        if category.is_valid():
            category.save()
            return Response({'status': 'successful'}, status=status.HTTP_200_OK)
        else:
            return Response(category.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['post'], detail=True)
    def remove_category(self, request, pk=None):
        category = RecipeCategory.objects.filter(recipe=pk, category=request.data['category'])
        try:
            category.delete()
            return Response({'status': 'successful'}, status=status.HTTP_200_OK)
        except:
            return Response(category.errors, status=status.HTTP_400_BAD_REQUEST)