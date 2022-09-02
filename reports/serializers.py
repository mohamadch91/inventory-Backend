from rest_framework import serializers
from .models import *
from rest_framework.validators import UniqueValidator

class gapSaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = gapSave
        fields = '__all__'

class plannedSerializer(serializers.ModelSerializer):
    class Meta:
        model = plannedGap
        fields = '__all__'
