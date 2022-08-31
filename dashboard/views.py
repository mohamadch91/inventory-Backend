from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from re import I
from django.shortcuts import render
from django.utils import timezone
# Create your views here.
import json
from os import stat
from urllib import response
from django.shortcuts import render
import datetime
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
from maintanance.models import *
from maintanance.serializers import *

class dashboarditemView(APIView):
    permission_classes=(IsAuthenticated,)
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
            item_type=ItemType.objects.filter(itemclass=x.id,active=True)
            second_data=[]
            for k in item_type:
                items=item.objects.filter(item_class=x.id,item_type=k.id)
                fil=items.filter(IsItFunctioning=True)
                
                working=0
                if(fil.count()==0):
                    working=0
                else:
                    working=fil.count()/items.count()
                data={
                    "item_type":k.title,
                    "total_items":items.count(),
                    "working":working,

                }
                second_data.append(data)
            if(len(second_data)==0):
                continue
            else:    
                new_data={
                    "item_class":x_ser.data["title"],
                    "items":second_data
                }
                first_data.append(new_data)    

        return Response(first_data,status=status.HTTP_200_OK)
    
class dashboardFacilityView(APIView):
        permission_classes=(IsAuthenticated,)
        def get(self,request):
            user=request.user
            facility=user.facilityid
            facility=get_object_or_404(Facility, id=facility.id)
            fac_ser=facilitySerializer(facility,many=False)
            level=facility.level.id
            levels_Ser=levelSerializer(level,many=True)
            all_fac=Facility.objects.all()
            ans=[]
            for x in all_fac:
                new_data={}
                if(x.id>=facility.id):
                    count=0
                    for y in all_fac:
                        if(y.id>x.id):
                            count+=1
                    defined=0        
                    lower=0
                    if(x.loverlevelfac!=None):
                        defined=count/x.loverlevelfac
                        lower=x.loverlevelfac
                    new_data={
                        "name":x.name,
                        "sub_fac":count,
                        "defined":"%.2f"%defined,
                        "lower":lower

                    }
                    ans.append(new_data)
            return Response(ans,status=status.HTTP_200_OK)            
class dahboardlevelView(APIView):
    permission_classes=(IsAuthenticated,)
    def get(self,request):
        user=request.user
        facility=user.facilityid
        facility=get_object_or_404(Facility, id=facility.id)
        fac_ser=facilitySerializer(facility,many=False)
        level=facility.level.id
        levels_Ser=levelSerializer(level,many=True)
        levels=LevelConfig.objects.all()
        first_ans=[]
        second_ans=[]
        for x in levels:
            if(x.id>=level):
                fac=Facility.objects.filter(level=x.id)
                fac_count=fac.count()
                count=0
                allow_count=0
                for y in fac:
                    new_data={}
                    if(y.id>=facility.id):
                        count=0
                        for z in fac:
                            if(z.id>y.id):
                                count+=1
                        defined=0        
                        lower=0
                        if(y.loverlevelfac!=None):
                            defined=count/y.loverlevelfac
                            lower=y.loverlevelfac
                        new_data={
                            "id":y.id,
                            "name":y.name,
                            "sub_fac":count,
                            "defined":"%.2f"%defined,
                            "lower":lower,
                            "update":y.updated_at,
                            "level_id":x.id,
                        "level_name":x.name,
                        }
                        second_ans.append(new_data)
                    if(y.loverlevelfac!=None):
                        allow_count+=y.loverlevelfac
                    subs=Facility.objects.filter(parentid=y.id)
                    count+=subs.count()
                data={
                    "level_id":x.id,
                    "level_name":x.name,
                    "total":fac_count,
                    "sub":allow_count,
                    "def":count
                }
                first_ans.append(data)
        final_data={
            "level_table":first_ans,
            "facility_table":second_ans
        }
        return Response(final_data,status=status.HTTP_200_OK)
        

class getitemmaintatnce(APIView):
    permission_classes=(IsAuthenticated,)
    def get(self,request):
        user=request.user
        facility=user.facilityid
        facility=get_object_or_404(Facility, id=facility.id)
        items=item.objects.filter(facility=facility.id)
        three_days=[]
        seven_days=[]
        for x in items:
            if(x.IsItFunctioning==False):
                continue
            if(x.MaintenanceGroup!=None):
                actievs=activeMaintance.objects.filter(maintanncegp=x.MaintenanceGroup)
                for y in actievs:
                    #calulate interval between now and last maintenance
                    main=y.maintanance
                    if(main.requires==True):
                    #minus now from created at
                        dayss=(timezone.now()-x.created_at).days
                        dayss=dayss%main.freq
                        dayss2=dayss%main.freq_in_loc
                        days=main.freq-dayss
                        days2=main.freq_in_loc-dayss2
                        if(days<=3 or days2<=3):
                            three_days.append(x.id)
                            #add this maintance to the list of maintance to be done
                            data={
                                "maintance":y.maintanance.id,
                                "item":x.id,
                                "maintanncegp":y.maintanncegp.id,
                            }
                            ser=toDoMaintanceSerializers(data=data)
                            if(ser.is_valid()):
                                ser.save()

                        elif(days<=7 or days2<=7):
                            seven_days.append(x.id)
                            #add this maintance to the list of maintance to be done
                            data={
                                "maintanance":y.maintanance.id,
                                "item":x.id,
                                "maintanncegp":y.maintanncegp.id,
                            }
                            ser=toDoMaintanceSerializers(data=data)
                            if(ser.is_valid()):
                                ser.save()
        todo=toDoMaintance.objects.all()
        counter=0
        days_extended=[]
        for x in todo:
            if(x.done==False):
                days=(timezone.now()-x.created_at).days
                if(days>=4):
                    counter+=1
                    days_extended.append(days)
        day=0
        if(days_extended!=[]):
            day=max(days_extended) 
        print(counter)
        return Response({"three_days":len(three_days),"seven_days":len(seven_days),"extended":{
            "max_extended":day,
            "count":counter
        }},status=status.HTTP_200_OK)

class todoMaintances(APIView):
    permission_classes=(IsAuthenticated,)
    def get(self,request):
        user=request.user
        facility=user.facilityid
        facility=get_object_or_404(Facility, id=facility.id)
        todo=toDoMaintance.objects.filter(item__facility=facility.id)
        ser=toDoMaintanceSerializers(todo,many=True)
        return Response(ser.data,status=status.HTTP_200_OK)
       


