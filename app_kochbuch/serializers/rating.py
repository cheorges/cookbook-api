from rest_framework import serializers

from app_kochbuch.models.rating import Rating
from app_kochbuch.serializers.user import UserSerializer


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'


class RatingDetailSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    user_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Rating
        fields = ('id', 'rating', 'date', 'title', 'comment', 'recipe', 'user', 'user_id')