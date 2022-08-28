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

class dashboarditemView(APIView):

    def get (self,request):
        user=request.user
        facility=user.facilityid
        facility=get_object_or_404(Facility, id=facility.id)
        fac_ser=facilitySerializer(facility,many=False)
        level=facility.level.id
        levels_Ser=levelSerializer(level,many=True)
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
                items=item.objects.filter(item_class=x.id,item_type=k.id)
                fil=items.filter(IsItFunctioning=True)
                data={
                    "item_type":k.name,
                    "total_items":items.count(),
                    "working":items.count()/fil.count(),

                }
                second_data.append(data)
            new_data={
                "item_class":x_ser.data["title"],
                "items":second_data
            }
            first_data.append(new_data)    

        return Response(first_data,status=status.HTTP_200_OK)
    