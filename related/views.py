from django.shortcuts import render

# Create your views here.
from re import I
from django.shortcuts import render

# Create your views here.
import json
from os import stat
from urllib import response
from django.shortcuts import render

# Create your views here.
from .serializers import *
from rest_framework.permissions import IsAuthenticated

from authen.models import User
from .models import *
from .serializers import *
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404


# Create your views here.
class relatedfacilityView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self,request):
        query_set=relatedFacility.objects.all()
        serializer = relatedfacilitySerilizer(query_set, many=True)
        return Response(serializer.data)
    def put(self, request):
        id=request.data["id"]
        country = get_object_or_404(relatedFacility, id=id)
        serializer = relatedfacilitySerilizer(country, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)