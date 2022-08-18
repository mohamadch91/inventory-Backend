from rest_framework import serializers
from .models import *

class HRSerializer(serializers.ModelSerializer):
    class Meta:
        model = HR
        fields = '__all__'