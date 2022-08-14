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

class fieldView(APIView):
    # permission_classes = (IsAuthenticated,)
    def get(self,request):
        query_set=Field.objects.all()
        serializer = fieldSerializer(query_set, many=True)
        return Response(serializer.data)    
    def put(self,request):
        id=request.data["id"]
        country = get_object_or_404(Field, id=id)
        serializer = fieldSerializer(country, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class relatedItemTypeView(APIView):
    # permission_classes = (IsAuthenticated,)
    def get(self,request):
        id=request.query_params.get('id', None)
        ans=None
        if(id==None):
            query_set=relatedItemType.objects.all()
            serializer = relatedItemTypeSerilizer(query_set, many=True)
            ans=serializer.data
        else:
            itemType=get_object_or_404(ItemType, id=id)
            query_set=relatedItemType.objects.filter(itemtype=itemType)
            serializer = relatedItemTypeSerilizer(query_set, many=True)
            ans=serializer.data
        final_ans=[]    
        for x in ans:
            field=get_object_or_404(Field, id=x['field'])
            itemtype=get_object_or_404(ItemType, id=x['itemtype'])
            field_serilize=fieldSerializer(field)
            itemtype_serilize=itemtypeSerializer(itemtype)
            x['field']=field_serilize.data
            x['itemtype']=itemtype_serilize.data
            final_ans.append(x)
        return Response(final_ans,status=status.HTTP_200_OK)    

    def put(self,request):
        ans=[]
        for x in request.data:
            enable=x['enable']
            if(enable):
                field=get_object_or_404(Field, id=x['fieldid'])
                itemtype=get_object_or_404(ItemType, id=x['itemtypeid'])
                obj=relatedItemType.objects.filter(field=x['fieldid'], itemtype=x['itemtypeid'])
                if(len(obj)==0):
                    data={
                        'field':field.id,
                        'itemtype':itemtype.id ,
                        'required':x['required']
                    }
                    serializer = relatedItemTypeSerilizer(data=data)
                    if serializer.is_valid():
                        serializer.save()
                        ans.append(serializer.data)
                    else:
                        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                else:
                    obj=relatedItemType.objects.filter(field=x['fieldid'], itemtype=x['itemtypeid'])
                    obj.update(required=x['required'])
                    # data={
                    #     "required":x['required'],
                    #     "itemtype":itemtype.id,
                    #     "field":field.id
                    # }
                    # ser=relatedItemTypeSerilizer(obj, data=data)
                    # if ser.is_valid():
                    #     ser.save()
                    #     ans.append(ser.data)
                    # else:
                    #     return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
                        
            else:

                obj=relatedItemType.objects.filter(field=x['fieldid'], itemtype=x['itemtypeid'])
                if(len(obj)==1):
                    obj.delete()
        return Response(ans,status=status.HTTP_200_OK)




