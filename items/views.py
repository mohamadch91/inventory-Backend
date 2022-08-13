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
from settings.serializers import *
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404


class itemclassView(APIView):
    permission_classes = (IsAuthenticated,)

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
        country = get_object_or_404(ItemClass, id=id)
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
    permission_classes = (IsAuthenticated,)

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
            id=request.data["id"]
            level = get_object_or_404(ItemType, id=id)
            serializer =  itemtypeSerializer(level, data=request.data)
            if serializer.is_valid():
                serializer.save()   
                return Response(serializer.data,status=status.HTTP_200_OK)    
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, *args, **kwargs):
        id=request.data["id"]
        level = get_object_or_404(ItemType, id=id)
        level.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)   

class itemtypeByclass(generics.ListAPIView):
    serializer_class = itemtypeSerializer
    queryset = ItemType.objects.all()
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        id=request.query_params.get('id', None)
        if(id==None):
            item_type=ItemType.objects.filter(active=True)
            serializer =  itemtypeSerializer(item_type, many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)      
        else:
            item_class=get_object_or_404(ItemClass, id=id)
            item_type=ItemType.objects.filter(itemclass=item_class,active=True)
            serializer =  itemtypeSerializer(item_type, many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)        

class itemTypeinLevels(APIView):

    def put(self,request):
        #if not exist add to data base
        if('id' not in request.data):
            serializer =  itemtypelevelSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
          
        else:
            item_type=get_object_or_404(Itemtypelevel, id=request.data["id"])
            serializer =  itemtypelevelSerializer(item_type, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)      
    def get(self,request):
        level=request.query_params.get('level', None)
        res=[]
        if(level==None): 
            level = Itemtypelevel.objects.all()
            for x in level:
                serializer =  itemtypelevelSerializer(x)
                print(serializer.data['itemtypeid'])
                itemtype=ItemType.objects.get(id=serializer.data['itemtypeid'])
                itemtype=itemtypeSerializer(itemtype,many=False)
                lev=LevelConfig.objects.get(id=serializer.data['level'])
                lev=levelSerializer(lev,many=False)
                data={
                    "id":serializer.data["id"],
                    "active":serializer.data["active"],
                    "itemtype":itemtype.data,
                    "level":lev.data,
                }
                res.append(data)
            return Response(res)
        else:
            level = Itemtypelevel.objects.filter(level=level)
            for x in level:
                serializer =  itemtypelevelSerializer(x)
                print(serializer.data['itemtypeid'])
                itemtype=ItemType.objects.get(id=serializer.data['itemtypeid'])
                itemtype=itemtypeSerializer(itemtype,many=False)
                lev=LevelConfig.objects.get(id=serializer.data['level'])
                lev=levelSerializer(lev,many=False)
                data={
                    "id":serializer.data["id"],
                    "active":serializer.data["active"],
                    "itemtype":itemtype.data,
                    "level":lev.data,
                }
                res.append(data)
            return Response(res)    