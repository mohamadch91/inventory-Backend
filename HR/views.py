from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
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

from facilities.serializers import facilitySerializer

# Create your views here.
from .serializers import *
from rest_framework.permissions import IsAuthenticated

from authen.models import User
from .models import *
from .serializers import *
from settings.serializers import *
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from facilities.models import *

class HRView(APIView):

    def get(self,request):
        f_id=request.query_params.get('id',None)
        if f_id is not None:
            country = HR.objects.filter(facility=f_id)
            serializer =  HRSerializer(country, many=True)
            return Response(serializer.data)
        country = HR.objects.all()
        serializer =  HRSerializer(country, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer =   HRSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def put(self, request):
        id=request.data["id"]
        country = get_object_or_404(HR, id=id)
        serializer =  HRSerializer(country, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request):
        id=request.data["id"]
        country = get_object_or_404(HR, id=id)
        country.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)            

class HRhelperView(APIView):
    
    def get(self,request):
        facility=Facility.objects.filter(parentid=request.user.facilityid.id)
        facility=Facility.objects.filter(id=request.user.facilityid.id)|facility
        ans=[]
        for x in facility:
            data={
                "id":x.id,
                "name":x.name
            }
            ans.append(data)
        return Response(ans)    