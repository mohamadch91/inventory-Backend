from dataclasses import field
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
from items.serializers import *
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from items.models import ItemType
from django.shortcuts import get_object_or_404

# Create your views here.
class pqs3View(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self,request):
        query_set=pqs3.objects.all()
        serializer = pqs3Serializer(query_set, many=True)
        return Response(serializer.data)    
    def post(self,request):
        pqs3.objects.all().delete()
        ans=[]
        for x in request.data:
            serializer = pqs3Serializer( data=x)
            if serializer.is_valid():
                serializer.save()
                ans.append(serializer.data)
            else:    
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(ans,status=status.HTTP_201_CREATED)
class pqs4View(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self,request):
        query_set=pqs4.objects.all()
        serializer = pqs4Serializer(query_set, many=True)
        return Response(serializer.data)    
    def post(self,request):
        pqs4.objects.all().delete()
        ans=[]
        for x in request.data:
            serializer = pqs4Serializer(data=x)
            if serializer.is_valid():
                serializer.save()
                ans.append(serializer.data)
            else:    
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(ans,status=status.HTTP_201_CREATED)