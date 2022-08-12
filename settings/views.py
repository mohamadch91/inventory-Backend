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


class CountryView(APIView):
    # permission_classes = (IsAuthenticated,)

    def post(self, request):
        query_set=CountryConfig.objects.all()
        print(len(query_set))
        if(len(query_set)>0):
            return Response("Country exist",status=status.HTTP_400_BAD_REQUEST)
        else:    
            serializer =   countrySerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        country = CountryConfig.objects.all()
        serializer =  countrySerializer(country, many=True)
        return Response(serializer.data)

    def put(self, request, ):
        id=request.data["id"]
        country = get_object_or_404(CountryConfig, id=id)
        serializer =  countrySerializer(country, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        id=request.data["id"]
        country = get_object_or_404(CountryConfig, id=id)
        country.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
class LevelView(APIView):
    # permission_classes = (IsAuthenticated,)

    def post(self, request):
        level=0
        country=CountryConfig.objects.all()
        #check country levels
        for i in country:
            x=countrySerializer(i,many=False)
            level=x.data["levels"]
        count=len(LevelConfig.objects.all())
        if(count==level):
            return Response("Level is greater than country level",status=status.HTTP_400_BAD_REQUEST)

        else:
            serializer =   levelSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        level = LevelConfig.objects.all()
        serializer =  levelSerializer(level, many=True)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        # rows=request.data["rows"]
        # print(rows)
        res=[]
        for x in request.data:      
            # print(x)  
            level = get_object_or_404(LevelConfig, id=x["id"])
            serializer =  levelSerializer(level, data=x)
            if serializer.is_valid():
                serializer.save()
                res.append(serializer.data)
            else:    
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(res,status=status.HTTP_200_OK)    

    def delete(self, request, *args, **kwargs):
        id=request.data["id"]
        level = get_object_or_404(LevelConfig, id=id)
        level.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)        
        