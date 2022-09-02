from rest_framework import serializers
from .models import *
from rest_framework.validators import UniqueValidator

class gapSaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = gapSave
        fields = '__all__'
