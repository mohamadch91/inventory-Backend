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

class facilityParamSerilizer(serializers.ModelSerializer):
    class Meta:
        model = facilityParam
        fields = '__all__'

class facilityParamDescriptionSerilizer(serializers.ModelSerializer):
    class Meta:
        model = facilityParamDescription
        fields = '__all__'        
class  itemParamSerilizer(serializers.ModelSerializer):
    class Meta:
        model = itemParam
        fields = '__all__'
class itemParamDescriptionSerilizer(serializers.ModelSerializer):
    class Meta:
        model = itemParamDescription
        fields = '__all__'           

class FacilityvalidationSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Facilityvalidation
        fields = '__all__'

class ItemvalidationSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Itemvalidation
        fields = '__all__'