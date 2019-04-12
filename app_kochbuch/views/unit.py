from rest_framework import viewsets, mixins, status
from rest_framework.decorators import action
from rest_framework.response import Response

from app_kochbuch.models.unit import Unit
from app_kochbuch.serializers.unit import UnitSerializer


class ViewUnit(mixins.ListModelMixin,
               mixins.RetrieveModelMixin,
               mixins.CreateModelMixin,
               mixins.UpdateModelMixin,
               viewsets.GenericViewSet):
    serializer_class = UnitSerializer
    queryset = Unit.objects.all()

    def delete(self, request, pk=None):
        try:
            self.get_object().delete()
        except:
            return Response({'error':'object is allready used'}, status.HTTP_400_BAD_REQUEST)
        return Response({'status':'successful'})