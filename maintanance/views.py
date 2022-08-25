from django.shortcuts import render

# Create your views here.
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

from items.serializers import itemclassSerializer

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
from items.serializers import *

class helperView(APIView):
    def get(self,request):

        item_class=ItemClass.objects.filter(active=True)
        ans=[]
        for x in item_class:
            item_type=ItemType.objects.filter(itemclass=x.id,active=True)
            type_ser=itemtypeSerializer(item_type,many=True)
            class_ser=itemclassSerializer(x)
            data={
                "item_class":class_ser.data,
                    "item_type":type_ser.data
            }
            ans.append(data)
        return Response(ans,status=status.HTTP_200_OK)


class maintananceView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):

            serializer =   maintanSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        item_class=request.query_params.get('item_class',None)
        item_type=request.query_params.get('item_type',None)
        if(item_class!=None and item_type!=None):
            item_class=get_object_or_404(ItemClass,id=item_class)
            item_type=get_object_or_404(ItemType,id=item_type)
            main=maintanance.objects.filter(item_class=item_class.id,item_type=item_type.id)
            ser=maintanSerializer(main,many=True)
            return Response(ser.data,status=status.HTTP_200_OK)
        country = maintanance.objects.all()
        serializer =  maintanSerializer(country, many=True)
        return Response(serializer.data)

    def put(self, request, ):
        id=request.data["id"]
        country = get_object_or_404(maintanance, id=id)
        serializer =  maintanSerializer(country, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        id=request.data["id"]
        country = get_object_or_404(maintanance, id=id)
        country.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


                