from rest_framework import viewsets

from app_kochbuch.models.category import Category
from app_kochbuch.serializers.category import CategorySerializer


class ViewCategory(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()