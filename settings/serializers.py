from rest_framework import serializers
from .models import *
from rest_framework.validators import UniqueValidator

class countrySerializer(serializers.ModelSerializer):
    class Meta:
        model = CountryConfig
        fields = '__all__'
        extra_kwargs = {

            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
        }

class levelSerializer(serializers.ModelSerializer):
    class Meta:
        model = LevelConfig
        fields = '__all__'
        extra_kwargs = {

            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
        }