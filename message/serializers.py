from rest_framework import serializers
from .models import *

class messageSerializer(serializers.ModelSerializer):
    class Meta:
        model = message
        fields = '__all__'
        