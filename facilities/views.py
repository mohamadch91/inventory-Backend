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
from item.models import *
import copy
class FacilityView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        new_data=copy.deepcopy(request.data)
        country=CountryConfig.objects.all()[0]
        country_code=country.codecountry
        level_code=new_data["level"]
        level_code =f"{level_code:02d}"
        facility_num=Facility.objects.filter(level=level_code).count()
        facility_num=facility_num+1
        facility_num=f"{facility_num:05d}"
        new_data["code"]=f"{country_code}{level_code}{facility_num}"
        new_data["country"]=country.id
        serializer =   facilitySerializer(data=new_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        id=request.query_params.get("id",None)
        if id is not None:
            facility = get_object_or_404(Facility, id=id)
            serializer = facilitySerializer(facility)
            return Response(serializer.data)
        country = Facility.objects.all()
        serializer =  facilitySerializer(country, many=True)
        return Response(serializer.data)

    def put(self, request, ):
        print(request)
        id=request.data["id"]
        country = get_object_or_404(Facility, id=id)
        serializer =  facilitySerializer(country, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        id=request.data["id"]
        facility = get_object_or_404(Facility, id=id)
        below=Facility.objects.filter(parentid=facility.id)
        if below.count()>0:
            return Response({"message": "Cannot delete facility with children"}, status=status.HTTP_400_BAD_REQUEST)
        item_num=item.objects.filter(facility=facility.id).count()
        if item_num>0:
            return Response({"message": "Cannot delete facility with items"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_204_NO_CONTENT)

class facilityFieldView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        
        user=request.user
        this_facility=Facility.objects.filter(id=user.facilityid.id)[0]
        parent_num=Facility.objects.filter(parentid=this_facility.id)
        parent_num=parent_num.count()
        if(parent_num>= this_facility.loverlevelfac):
            return Response("You have reached the maximum number of facilities you can add",status=status.HTTP_403_FORBIDDEN)

        level=this_facility.level
        allow_levels=LevelConfig.objects.filter(id__gt=level.id)
        if(allow_levels.count()==0):
            return Response ("you cannot add facility at this level",status=status.HTTP_403_FORBIDDEN)
        levels_Ser=levelSerializer(allow_levels,many=True)
        rel=relatedFacility.objects.filter(active=True)
        ans=[]
        for x in rel:
            if(x.id==1 or x.id ==3):
                continue
            param=facilityParam.objects.filter(fieldid=x.id).order_by('order')
            desc_ser=[]
            
            for y in param:
                desc=facilityParamDescription.objects.filter(paramid=y.id).order_by('order')
                desc_ser=facilityParamDescriptionSerilizer(desc,many=True)
            data={}    
            if(desc_ser==[]):
                     data={
                "id":x.id,
                "name":x.name,
                "topic":x.topic,
                "type":x.type,
                "active":x.active,
                "required":x.required,
                "stateName":x.state,
                "params":[]
                     }
            else:         
                data={
                    "id":x.id,
                    "name":x.name,
                    "topic":x.topic,
                    "type":x.type,
                    "active":x.active,
                    "required":x.required,
                    "stateName":x.state,
                    "params":desc_ser.data
                }
            val=Facilityvalidation.objects.filter(fieldid=x.id)
            val_ser=FacilityvalidationSerilizer(val,many=True)
            if(val.count()>0):
                data["validation"]=val_ser.data
            else:
                data["validation"]=[]    
            ans.append(data)
        data={
            "levels":levels_Ser.data,
            "related":ans
        }
        return Response(data,status=status.HTTP_200_OK)





        

 