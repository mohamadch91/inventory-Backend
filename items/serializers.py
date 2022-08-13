from rest_framework import serializers
from .models import *

class itemclassSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemClass
        fields = '__all__'
        # fields = ('id', 'title', 'code','active', 'created_at', 'updated_at')
        # extra_kwargs = {
        #     'created_at': {'read_only': True},
        #     'updated_at': {'read_only': True},
        # }

class itemtypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemType
        fields = '__all__'
        # fields = ('id', 'name', 'description', 'created_at', 'updated_at')
        # extra_kwargs = {
        #     'created_at': {'read_only': True},
        #     'updated_at': {'read_only': True},
        # }        
class itemtypelevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Itemtypelevel
        fields = '__all__'
        # fields = ('id', 'itemtypeid', 'level', 'created_at', 'updated_at')
        # extra_kwargs = {
        #     'created_at': {'read_only': True},
        #     'updated_at': {'read_only': True},
        # }        