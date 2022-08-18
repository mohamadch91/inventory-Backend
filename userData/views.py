import re
from django.shortcuts import render
from authen.models import *
from settings.models import *
from authen.serializers import *
from settings.serializers import *
# Create your views here.'
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from message.models import *
from message.serializers import *
class userDataView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset=User.objects.all() 
    def get(self, request):
        user = request.user
        user_serializer = UserSerializer(user)
        cs = countrySerializer(CountryConfig.objects.all(), many=True)
        messgaes=message.objects.filter(reciever=user.facilityid)
        serializer = messageSerializer(messgaes, many=True)
        res={
            "User":user_serializer.data,
            "Country":cs.data,
            "Messages":serializer.data
        }
        return Response(res,status=status.HTTP_200_OK)

