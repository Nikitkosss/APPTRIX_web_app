from django.contrib.auth import get_user_model
from rest_framework import serializers

from api.models import Coin, News

User = get_user_model()


class CoinSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Coin


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = News
