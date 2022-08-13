from django.shortcuts import render

# Create your views here.

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


class itemclassView(APIView):
    # permission_classes = (IsAuthenticated,)

    def post(self, request):
 
            serializer =   itemclassSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        country = ItemClass.objects.all()
        serializer =  itemclassSerializer(country, many=True)
        return Response(serializer.data)

    def put(self, request, ):
        id=request.data["id"]
        country = get_object_or_404(itemclassSerializer, id=id)
        serializer =  itemclassSerializer(country, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        id=request.data["id"]
        country = get_object_or_404(itemclassSerializer, id=id)
        country.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
class itemtypeView(APIView):
    # permission_classes = (IsAuthenticated,)

    def post(self, request):

            serializer =   itemtypeSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        level = ItemType.objects.all()
        serializer =  itemtypeSerializer(level, many=True)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):

            level = get_object_or_404(ItemType, id=x["id"])
            serializer =  itemtypeSerializer(level, data=x)
            if serializer.is_valid():
                serializer.save()   
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response(res,status=status.HTTP_200_OK)    

    def delete(self, request, *args, **kwargs):
        id=request.data["id"]
        level = get_object_or_404(ItemType, id=id)
        level.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)        
        