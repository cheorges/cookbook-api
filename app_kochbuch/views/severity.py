from rest_framework import viewsets, mixins, status
from rest_framework.response import Response

from app_kochbuch.models.severity import Severity
from app_kochbuch.serializers.severity import SeveritySerializer


class ViewSeverity(mixins.ListModelMixin,
               mixins.RetrieveModelMixin,
               mixins.CreateModelMixin,
               mixins.UpdateModelMixin,
               viewsets.GenericViewSet):
    serializer_class = SeveritySerializer
    queryset = Severity.objects.all()

    def delete(self, request, pk=None):
        try:
            self.get_object().delete()
        except:
            return Response({'error':'object is allready used'}, status.HTTP_400_BAD_REQUEST)
        return Response({'status':'successful'})