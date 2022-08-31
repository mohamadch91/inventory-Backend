
from dataclasses import fields
from rest_framework import serializers
from .models import *

class maintanSerializer(serializers.ModelSerializer):

        class Meta:
            model = maintanance
            fields = '__all__'
     
     
class activemainSerializers(serializers.ModelSerializer):
    class Meta:
        model=activeMaintance
        fields='__all__'     

class maintancegpSerializers(serializers.ModelSerializer):
    class Meta:
        model=maintancegp
        fields='__all__'

class toDoMaintanceSerializers(serializers.ModelSerializer):
    class Meta:
        model=toDoMaintance
        fields='__all__'

class doneMaintanceSerializers(serializers.ModelSerializer):
    class Meta:
        model=doneMaintance
        fields='__all__'
        