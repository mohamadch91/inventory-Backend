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
            active=True
            title=None
            havePQs=False
            item_class=None
            if('active' in request.data):
                active=request.data["active"]
            if('title' in request.data):
                title=request.data["title"]
            if('havePQS' in request.data):
                havePQs=request.data["havePQS"]
            if('itemclass' in request.data):
                item_class=request.data["itemclass"]

            obj={
                "title":title,
                "active":active,
                "havePQS":havePQs,
                "itemclass":item_class
            }
            item_class=ItemClass.objects.get(id=obj["itemclass"])
            num=item_class.itemtype_set.count()
            print(num)
            #set code for alll item classes
            if(item_class.id==1):
                obj["code"]="AC"+str(num-7+1)
            elif item_class.id==2 :
                obj["code"]="PC"+str(num-3+1)
            elif item_class.id==3 :
                obj["code"]="TM"+str(num-4+1)
            elif item_class.id==4 :
                obj["code"]="EL"+str(num-2+1)
            elif item_class.id==5 :
                obj["code"]="ET"+str(num-5+1)
            elif item_class.id==6 :
                obj["code"]="TR"+str(num-10+1)
            elif item_class.id==7 :
                obj["code"]="CA"+str(num+1)
            elif item_class.id==8 :
                obj["code"]="CB"+str(num+1)
            elif item_class.id==9 :
                obj["code"]="CC"+str(num+1)
            elif item_class.id==10 :
                obj["code"]="CD"+str(num+1)
                
            serializer =  itemtypeSerializer(data=obj)
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
            ans=[]
            item_class=ItemClass.objects.filter(active=True)
            for x in item_class:
                cser=itemclassSerializer(x)
                item_type=ItemType.objects.filter(itemclass=x.id,active=True)

                serializer =  itemtypeSerializer(item_type, many=True)
                data={
                    "item_class":cser.data,
                    "item_type":serializer.data
                }
                # print(data)
                ans.append(data)
            return Response(ans,status=status.HTTP_200_OK)        

class itemTypeinLevels(APIView):
    permission_classes = (IsAuthenticated,)
    def put(self,request):
        ans=[]
        for x in request.data:
            if('id' not in x):
                serializer =  itemtypelevelSerializer(data=x)
                if serializer.is_valid():
                    serializer.save()
                    ans.append(serializer.data)
                else:    
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
            else:
                item_type=get_object_or_404(Itemtypelevel, id=x["id"])
                serializer =  itemtypelevelSerializer(item_type, data=x)
                if serializer.is_valid():
                    serializer.save()
                    ans.append(serializer.data)
                else:    
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
        return Response(ans,status=status.HTTP_200_OK)                
        
    def get(self,request):
        level=request.query_params.get('level', None)
        res=[]
        if(level==None): 
            level = Itemtypelevel.objects.all()
            # print(len(level))
            
            if(level!=None):
                for x in level:
                    serializer =  itemtypelevelSerializer(x)
                    # print(serializer.data)
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
                # print(serializer.data['itemtypeid'])
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

class manufacturerView(APIView):
        
    def get(self,request):
        id=request.query_params.get('id',None)
        if(id==None):
            return Response("need query param",status=status.HTTP_400_BAD_REQUEST)

        item_class=ItemClass.objects.filter(active=True,id=id)
        ans=[]
        for x in item_class:
            ser=itemclassSerializer(x)
            manufacturer=Manufacturer.objects.filter(itemclass=x.id)
            serializer =  ManufacturerSerializer(manufacturer, many=True)
            data={
                "item_class":ser.data,
                "manufacturer":serializer.data
            }
            ans.append(data)
        return Response(ans,status=status.HTTP_200_OK) 
    def post(self,request):
        ser=ManufacturerSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
    def put(self,request):
        id=request.data["id"]
        manufacturer = get_object_or_404(Manufacturer, id=id)
        serializer =  ManufacturerSerializer(manufacturer, data=request.data)
        if serializer.is_valid():
            serializer.save()   
            return Response(serializer.data,status=status.HTTP_200_OK)    
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)        

class manhelper(APIView):
    def get(self,request):
        item_class=ItemClass.objects.filter(active=True)
        ser=itemclassSerializer(item_class,many=True)
        return Response(ser.data)