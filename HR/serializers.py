from rest_framework import serializers
from .models import *

# class helpSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Help
#         fields = '__all__'
#         # fields = ('id', 'title', 'code','active', 'created_at', 'updated_at')
#         # extra_kwargs = {
#         #     'created_at': {'read_only': True},
#         #     'updated_at': {'read_only': True},
#         # }

