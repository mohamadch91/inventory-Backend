from rest_framework import serializers
from .models import *
from rest_framework.validators import UniqueValidator

class pqs3Serializer(serializers.ModelSerializer):
    class Meta:
        model = pqs3
        fields = '__all__'
        # fields = ('id', 'title', 'code','active', 'created_at', 'updated_at')
        # extra_kwargs = {
        #     'created_at': {'read_only': True},
        #     'updated_at': {'read_only': True},
        # }
class pqs4Serializer(serializers.ModelSerializer):
    class Meta:
        model = pqs4
        fields = '__all__'
        # fields = ('id', 'title', 'code','active', 'created_at', 'updated_at')
        # extra_kwargs = {
        #     'created_at': {'read_only': True},
        #     'updated_at': {'read_only': True},
        # }        