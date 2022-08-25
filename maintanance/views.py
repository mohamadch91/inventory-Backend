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
import copy 
class helperView(APIView):
    def get(self,request):
            item_class=ItemClass.objects.filter(active=True)
            first_data=[]
            for x in item_class:
                x_ser=itemclassSerializer(x)
                item_type=ItemType.objects.filter(itemclass=x.id,active=True )
                second_data=[]
                for k in item_type:
                    new_data={
                        "id":k.id,
                        "title":k.title,
                        "havepqs":k.havePQS,
                    }
                    second_data.append(new_data)
                data={
                    "item_class":{
                        "id":x.id,
                        "title":x.title,

                    },
                    "item_type":second_data,
                }
                first_data.append(data)
            return Response(first_data)


class maintananceView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
            new_data=copy.deepcopy(request.data)
            item_class=get_object_or_404(ItemClass,id=new_data['item_class'])
            item_type=get_object_or_404(ItemType,id=new_data['item_type'])
            item_code=f"{maintanance.objects.count()+1:03d}"    
            new_data["code"]=f"{item_class.code}{item_type.code}{item_code}"

            serializer =   maintanSerializer(data=new_data)
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


                