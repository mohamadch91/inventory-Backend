from rest_framework import serializers
from .models import *

class facilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Facility
        fields = '__all__'
     