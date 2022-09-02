from rest_framework import serializers
from .models import *
from rest_framework.validators import UniqueValidator

class gavSaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = gapSave
        fields = '__all__'
        # fields = ('id', 'title', 'code','active', 'created_at', 'updated_at')
        # extra_kwargs = {
        #     'created_at': {'read_only': True},
        #     'updated_at': {'read_only': True},
        # }
