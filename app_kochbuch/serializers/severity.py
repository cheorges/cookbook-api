from rest_framework import serializers

from app_kochbuch.models.severity import Severity


class SeveritySerializer(serializers.ModelSerializer):
    class Meta:
        model = Severity
        fields = '__all__'
