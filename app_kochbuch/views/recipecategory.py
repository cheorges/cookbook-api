from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, mixins

from app_kochbuch.models.recipecategory import RecipeCategory
from app_kochbuch.serializers.recipecategory import RecipeCategorySerializer, RCRecipeDetailSerializer, \
    RCDetailSerializer


class ViewRecipeCategory(viewsets.ModelViewSet):
    serializer_class = RecipeCategorySerializer
    queryset = RecipeCategory.objects.all()
    filter_backends = (DjangoFilterBackend, )
    filter_fields = ('category',)

    def get_serializer_class(self):
        if self.detail:
            return RCDetailSerializer
        if self.request.GET.get('category',0):
            return RCRecipeDetailSerializer
        return RecipeCategorySerializer