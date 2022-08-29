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
        all_fac=Facility.objects.all()
        fac_ans=[]
        for x in all_fac:
            if(x.parentid is not None):
                if(x.parentid.id>=facility.id):
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
        working=itemParamDescription.objects.filter(paramid=11)
        working_ser=itemParamDescriptionSerilizer(working,many=True)
        phy=itemParamDescription.objects.filter(paramid=11)
        phy_ser=itemParamDescriptionSerilizer(phy,many=True)
        users=User.objects.all()
        user_Data=[]
        for i in users:
            if(i.facilityid.id>=facility.id):
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
        

        




