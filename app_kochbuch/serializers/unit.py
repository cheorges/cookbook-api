from rest_framework import serializers

from app_kochbuch.models.unit import Unit


class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = '__all__'