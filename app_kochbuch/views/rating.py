from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from app_kochbuch.models.rating import Rating
from app_kochbuch.serializers.rating import RatingSerializer, RatingDetailSerializer


class ViewRating(viewsets.ModelViewSet):
    serializer_class = RatingDetailSerializer
    queryset = Rating.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('user', 'recipe')