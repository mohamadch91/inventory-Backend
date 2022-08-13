from rest_framework import serializers
from .models import *
from rest_framework.validators import UniqueValidator

class relatedfacilitySerilizer(serializers.ModelSerializer):
    class Meta:
        model = relatedFacility
        fields = '__all__'

class fieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Field
        fields = '__all__'
 
class relatedItemTypeSerilizer(serializers.ModelSerializer):
    class Meta:
        model = relatedItemType
        fields = '__all__'
