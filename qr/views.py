from django.shortcuts import render

# Create your views here.
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

# Create your views here.
from authen.serializers import *
from rest_framework.permissions import IsAuthenticated

from authen.models import User
from .models import *
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from related.serializers import *
from facilities.serializers import *
from related.models import *
from settings.models import *
from settings.serializers import *
from item.models import *
from items.serializers import *

class QRhelperview(APIView):
    permission_classes=(IsAuthenticated,)
    def get(self,request):
        user=request.user
        facility=user.facilityid
        facility=get_object_or_404(Facility, id=facility.id)
        all_fac=Facility.objects.filter(parentid=facility.id,is_deleted=False)
        all_fac=Facility.objects.filter(id=facility.id)|all_fac
        fac_ans=[]
        fac_ans.append({
            "id":facility.id,
            "name":facility.name,
        })
        for x in all_fac:
            if(x.parentid is not None):
                if(x.parentid.id==facility.id or x.id==facility.id):
                    data={
                        "name":x.name,
                        "id":x.id,
                    }
                    fac_ans.append(data)
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
        working=itemParamDescription.objects.filter(paramid=11,enabled=True)
        working_ser=itemParamDescriptionSerilizer(working,many=True)
        phy=itemParamDescription.objects.filter(paramid=9,enabled=True)
        phy_ser=itemParamDescriptionSerilizer(phy,many=True)
        
        users=User.objects.filter(facilityid__in=all_fac)
        user_Data=[]
        for i in users:
                data={
                    "name":i.username,
                    "id":i.pk
                }
                user_Data.append(data)

        final_ans={
            "facility":fac_ans,
            "items":first_data,
            "working":working_ser.data,
                "physical":phy_ser.data,
                "users":user_Data
            
        }   
        return Response(final_ans,status=status.HTTP_200_OK)     

class generateQrView(APIView):
    permission_classes=(IsAuthenticated,)
    def get (self,request):
        facility=request.query_params.get('facility',None)
        item_class=request.query_params.get('item_class',None)
        item_type=request.query_params.get('item_type',None)
        physical=request.query_params.get('physical',None)
        working=request.query_params.get('working',None)
        user=request.query_params.get('user',None)
        year_from=request.query_params.get('year_from',None)
        year_to=request.query_params.get('year_to',None)
        code=request.query_params.get('code',None)
        func=request.query_params.get('func',None)
        items=item.objects.all()
        if(facility is not None):
            items=items.filter(facility=facility)
        else:
            items=item.objects.filter(facility=request.user.facilityid,isDel=False)    
        if(item_type is not None):
            items=items.filter(item_type=item_type)
        if(item_class is not None):
            items=items.filter(item_class=item_class)
        if(physical is not None):
            items=items.filter(PhysicalConditions=physical)
        if(working is not None):
            items=items.filter(WorkingConditions=working)

        if(year_from is not None):
            items=items.filter(YearInstalled__gte=year_from)
        if(year_to is not None):
            items=items.filter(YearInstalled__lte=year_to)
        if(code is not None):
            items=items.filter(code=code)
        if(func is not None):
            if(func=="true"):
                items=items.filter(IsItFunctioning=True)
            else:
                items=items.filter(IsItFunctioning=False)
        ans=[]
        for x in items:
            data={
                "id":x.id,
                "item_class":x.item_class.title,
                "item_type":x.item_type.title,
                "pqs_code":x.Model,
                "code":x.code,
                "qr":x.code,

            }        
            ans.append(data)
        return Response(ans,status=status.HTTP_200_OK)

class getqrView(APIView):
    def get (self,request):
        code=request.query_params.get('code',None)
        if(code is None):
            return Response('need query param',status=status.HTTP_400_BAD_REQUEST)
        x=item.objects.filter(code=code,isDel=False)[0]
        data={
                "id":x.id,
                "item_class":x.item_class.title,
                "item_type":x.item_type.title,
                "pqs_code":x.Model,
                "code":x.code,
                "qr":x.code,

            }
        return Response(data,status=status.HTTP_200_OK)




                
        

        




