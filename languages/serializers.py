from rest_framework import serializers
from .models import *

class languageSerializer(serializers.ModelSerializer):
    class Meta:
        model = languages
        fields = '__all__'

class languageWordSerializer(serializers.ModelSerializer):
    class Meta:
        model = languages_words
        fields = '__all__'        