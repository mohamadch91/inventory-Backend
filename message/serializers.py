from rest_framework import serializers
from .models import *

class messageSerializer(serializers.ModelSerializer):
    class Meta:
        model = message
        fields = '__all__'

class readedMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = readedMessage
        fields = '__all__'