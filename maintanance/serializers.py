
from rest_framework import serializers
from .models import *

class maintanSerializer(serializers.ModelSerializer):

        class Meta:
            model = maintanance
            fields = '__all__'
     
     