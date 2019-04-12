from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, mixins

from app_kochbuch.models.favourite import Favourite
from app_kochbuch.serializers.favourite import FavouriteSerializer, FavouriteDetailSerializer


class ViewFavourite(viewsets.ModelViewSet):
    serializer_class = FavouriteSerializer
    queryset = Favourite.objects.all()
    filter_backends = (DjangoFilterBackend, )
    filter_fields = ('user',)


    def get_serializer_class(self):
        if self.detail:
            return FavouriteSerializer
        if self.request.GET.get('user',0):
            return FavouriteDetailSerializer
        return FavouriteSerializer