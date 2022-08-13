from rest_framework import serializers
from .models import *
from rest_framework.validators import UniqueValidator

class relatedfacilitySerilizer(serializers.ModelSerializer):
    class Meta:
        model = relatedFacility
        fields = '__all__'
        extra_kwargs = {

            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
        }
