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
from related.serializers import *
from related.models import *
from settings.models import *
from settings.serializers import *
from facilities.models import *
from facilities.serializers import *
from items.models import *
from items.serializers import *

import copy

class itemView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        
        new_data=copy.deepcopy(request.data)
        facility=new_data["facility"]
        facility=get_object_or_404(Facility, id=facility)
        item_class=new_data["item_class"]
        item_type=new_data["item_type"]
        item_class=get_object_or_404(ItemClass, id=item_class)
        item_type=get_object_or_404(ItemType, id=item_type)   
        item_code=f"{item.objects.count()+1:03d}"    
        new_data["code"]=f"{facility.code}{item_class.code}{item_type.code}{item_code}"
        serializer = itemSerializer(data=new_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        id=request.query_params.get('id',None)
        if(id is not None):
                
            country = item.objects.filter(id=id)
            serializer =  itemSerializer(country, many=True)
            return Response(serializer.data)

        country = item.objects.all()
        serializer =  itemSerializer(country, many=True)
        return Response(serializer.data)

    def put(self, request, ):
        id=request.data["id"]
        country = get_object_or_404(item, id=id)
        serializer =  itemSerializer(country, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        id=request.data["id"]
        facility = get_object_or_404(item, id=id)
        facility.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class itemFieldView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        user=request.user
        class_id=request.query_params.get('class_id', None)
        type_id=request.query_params.get('type_id', None)
        if class_id is None and type_id is None:
            facility=user.facilityid
            facility=get_object_or_404(Facility, id=facility.id)
            level=facility.level.id
            item_type_id=[]
            itemTypeinlevels=Itemtypelevel.objects.filter(level=level,active=True)
            for x in itemTypeinlevels:
                item_type_id.append(x.itemtypeid.id)
            item_class=ItemClass.objects.filter(active=True)
            first_data=[]
            for x in item_class:
                x_ser=itemclassSerializer(x)
                item_type=ItemType.objects.filter(itemclass=x.id,active=True,id__in=item_type_id)
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
        else:
            item_class=get_object_or_404(ItemClass,id=class_id)
            item_type=get_object_or_404(ItemType,id=type_id)
            ans={}
            Manufacturers=Manufacturer.objects.filter(active=True,itemclass=item_class.id)
            man_Ser=ManufacturerSerializer(Manufacturers,many=True)    
            related=relatedItemType.objects.filter(itemtype=item_type.id)
            fields=[]
            for x in related:
                data={}
                field=Field.objects.filter(id=x.field.id)[0]
                field_ser=fieldSerializer(field,many=False)
                data["field"]=field_ser.data
                if(field.id==2):
                   
                    data["params"]=man_Ser.data
                else:
                   param=itemParam.objects.filter(fieldid=field.id)[0]
                   describe=itemParamDescription.objects.filter(paramid=param.id,enabled=True)
                   des_ser=itemParamDescriptionSerilizer(describe,many=True) 
                   data["params"]=des_ser.data
                fields.append(data)
            return Response(fields)       





        