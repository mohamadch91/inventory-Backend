from django.shortcuts import render

# Create your views here.

from copy import copy
from django.shortcuts import render

# Create your views here.

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
import copy

class messageView(APIView):
    def get(self,request):
        id=request.query_params.get('id',None)
        if id is not None:
            message = message.objects.filter(id=id)
            serializer =  messageSerializer(message, many=True)
            return Response(serializer.data)
        message = message.objects.all()
        serializer =  messageSerializer(message, many=True)
        return Response(serializer.data)
    def post(self, request):
        new_data=copy.deepcopy(request.data)
        user=request.data["user"]
        facility=Facility.objects.filter(id=user.facilityid)[0]
        new_data["sender"]=facility.id
        recievers=request.data["reciever"]
        for x in recievers:
            new_data["reciever"]=x
            serializer =  messageSerializer(data=new_data)
            if serializer.is_valid():
                serializer.save()
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response("messages sent succesfuly",status=status.HTTP_200_OK)
    def put(self, request):
        id=request.data["id"]
        message = get_object_or_404(messageSerializer, id=id)
        serializer =  messageSerializer(message, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request):
        id=request.data["id"]
        message = get_object_or_404(messageSerializer, id=id)
        message.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)