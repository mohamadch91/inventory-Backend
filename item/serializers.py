from rest_framework import serializers
from .models import *

class itemSerializer(serializers.ModelSerializer):
    class Meta:
        model = item
        fields = '__all__'
