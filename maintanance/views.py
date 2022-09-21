from cgitb import enable
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
from .serializers import *
from settings.serializers import *
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from items.serializers import *
from .models import maintancegp
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
                    mgp=maintancegp.objects.filter(item_class=x.id,item_type=k.id,enable=True)
                    mgp_Ser=maintancegpSerializers(mgp,many=True)
                    new_data={
                        "id":k.id,
                        "title":k.title,
                        "havepqs":k.havePQS,
                        "maintancegp":mgp_Ser.data
                    }
                    second_data.append(new_data)
                data={
                    "item_class":{
                        "id":x.id,
                        "title":x.title,

                    },
                    "item_type":second_data,
                }
                if(len(second_data)>0):
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


class maintancegpView(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request):
            new_data=copy.deepcopy(request.data)
            serializer =   maintancegpSerializers(data=new_data)
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
            main=maintancegp.objects.filter(item_class=item_class.id,item_type=item_type.id)
            ser=maintanSerializer(main,many=True)
            return Response(ser.data,status=status.HTTP_200_OK)
        country = maintancegp.objects.all()
        serializer =  maintancegpSerializers(country, many=True)
        return Response(serializer.data)

    def put(self, request, ):
        id=request.data["id"]
        country = get_object_or_404(maintancegp, id=id)
        serializer =  maintancegpSerializers(country, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        id=request.data["id"]
        country = get_object_or_404(maintancegp, id=id)
        country.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class activemainView(APIView):
    def get (self,request):
        item_class=request.query_params.get('item_class',None)
        item_type=request.query_params.get('item_type',None)
        gp=request.query_params.get('gp',None)
        main=maintanance.objects.filter(item_class=item_class,item_type=item_type,enable=True)
        final_ans=[]
        for x in main:
            x_ser=maintanSerializer(x,many=False)
            data={
                "maintance":x_ser.data
            }
            actives=activeMaintance.objects.filter(maintanance=x.id,maintanncegp=gp)
            if(actives.count()>0):
                data["assigned"]=True
            else:
                data["assigned"]=False
            final_ans.append(data)
        return Response(final_ans,status=status.HTTP_200_OK)   
    def post(self,request):
        ans=[]             
        for x in request.data:
            print(x)
            if(x["enable"]):
                actives=activeMaintance.objects.filter(maintanance=x["id"],maintanncegp=x["gp"])
                if(actives.count()>0):
                    pass
                else:
                    data={
                        "maintanance":x["id"],
                        "enable":True,
                        "maintanncegp":x["gp"]
                    }
                    ser=activemainSerializers(data=data)
                    if(ser.is_valid()):
                        ser.save()
                        ans.append(ser.data)
            else:
                actives=activeMaintance.objects.filter(maintanance=x["id"],maintanncegp=x["gp"])
                if(actives.count()>0):
                    main=get_object_or_404(activeMaintance,maintanance=x["id"],maintanncegp=x["gp"])
                    main.delete()
                else:
                    pass
        return Response(ans,status=status.HTTP_207_MULTI_STATUS)            
                
