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
                items=item.objects.filter(item_class=x.id,item_type=k.id,facility=facility.id)
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
                    "not_working":items.count()-fil.count(),

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
            all_fac=Facility.objects.filter(parentid=facility.id,is_functioning=True,is_deleted=False)
            all_fac=Facility.objects.filter(id=facility.id)|all_fac 
            ans=[]
            for x in all_fac:
                new_data={}
                if(x.id>=facility.id):
                    count=0
                    for y in all_fac:
                        if(y.parentid is not None):
                            if(y.parentid.id==x.id ):
                                count+=1
                    defined=0        
                    lower=0
                    if(x.loverlevelfac!=None and x.loverlevelfac!=0):
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
        counter=CountryConfig.objects.all()[0]
        levels=levels.filter(id__lte=counter.levels)
        first_ans=[]
        second_ans=[]
        for x in levels:
            if(x.id>=level):
                fac=Facility.objects.filter(level=x.id,parentid=facility.id,is_deleted=False,is_functioning=True)
                # fac=Facility.objects.filter(id=facility.id)|fac
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
                        if(y.loverlevelfac!=None and y.loverlevelfac!=0):
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
        counter2=0
        for x in items:
            if(x.IsItFunctioning==False):
                continue
            if(x.MaintenanceGroup!=None):
                counter2+=1
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
                            #add this maintance to the list of maintance to be done
                            data={
                                "maintanance":y.maintanance.id,
                                "item":x.id,
                                "maintanncegp":y.maintanncegp.id,
                            }
                            try:
                                obj=get_object_or_404(toDoMaintance,maintanance=y.maintanance.id,item=x.id,maintanncegp=y.maintanncegp.id)
                                new_day=(timezone.now()-obj.updated_at).days
                                if(new_day>=4):
                                    obj.done=False
                                    obj.save()
                                    three_days.append(x.id)
                            except:        
                                ser=toDoMaintanceSerializers(data=data)
                                if(ser.is_valid()):
                                    ser.save()
                                three_days.append(x.id)

                        elif(days<=7 or days2<=7):
                            #add this maintance to the list of maintance to be done
                            data={
                                "maintanance":y.maintanance.id,
                                "item":x.id,
                                "maintanncegp":y.maintanncegp.id,
                            }
                            try:
                                obj=get_object_or_404(toDoMaintance,maintanance=y.maintanance.id,item=x.id,maintanncegp=y.maintanncegp.id)
                                new_day=(timezone.now()-obj.updated_at).days
                                if(new_day>=8):
                                    obj.done=False
                                    obj.save()
                                    three_days.append(x.id)
                            except:        
                                ser=toDoMaintanceSerializers(data=data)
                                if(ser.is_valid()):
                                    ser.save()
                                    seven_days.append(x.id)

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
        return Response({"defined":counter2,"three_days":len(three_days),"seven_days":len(seven_days),"extended":{
            "max_extended":day,
            "count":counter
        }},status=status.HTTP_200_OK)

class todoMaintances(APIView):
    permission_classes=(IsAuthenticated,)
    def get(self,request):
        day=request.query_params.get('day')
        if(day is None):
            return Response({"error":"day is required"},status=status.HTTP_400_BAD_REQUEST)
        user=request.user
        facility=user.facilityid
        facility=get_object_or_404(Facility, id=facility.id)
        todo=toDoMaintance.objects.filter(item__facility=facility.id,done=False)
        ans=[]
        if(day=="3" or day=="7"):
            for x in todo:
                dayss=(timezone.now()-x.item.created_at).days
                dayss=dayss%x.maintanance.freq
                dayss2=dayss%x.maintanance.freq_in_loc
                days=x.maintanance.freq-dayss
                days2=x.maintanance.freq_in_loc-dayss2
                if(day=="3"):
                    deadline=x.created_at+datetime.timedelta(days=days)
                    deadline1=x.created_at+datetime.timedelta(days=days2)
                elif(day=="7"):
                    deadline=x.created_at+datetime.timedelta(days=days)
                    deadline1=x.created_at+datetime.timedelta(days=days2)
            
                data={
                    "id":x.id,
                    "code":x.item.code,
                    "interval":x.maintanance.freq,
                    "loc_interval":x.maintanance.freq_in_loc,
                    "deadline":str(deadline).split(" ")[0],
                    "deadline_in_loc":str(deadline1).split(" ")[0],
                    "name":x.maintanance.name,
                    
                }
                ans.append(data)
        elif(day=="extended"):
            for x in todo:
                if(x.done==False):
                    days1=(timezone.now()-x.created_at).days
                    dayss=(timezone.now()-x.item.created_at).days
                    dayss=dayss%x.maintanance.freq
                    dayss2=dayss%x.maintanance.freq_in_loc
                    days=x.maintanance.freq-dayss
                    days2=x.maintanance.freq_in_loc-dayss2
                    if(days1>=4):
                        
                        data={
                            "id":x.id,
                            "code":x.item.code,
                            "interval":x.maintanance.freq,
                            "loc_interval":x.maintanance.freq_in_loc,
                            "deadline":str(x.created_at+datetime.timedelta(days=days)).split(" ")[0],
                            "deadline_in_loc":str(x.created_at+datetime.timedelta(days=days2)).split(" ")[0],
                            "extended":(timezone.now()-x.created_at-datetime.timedelta(days=3)).days,
                            "name":x.maintanance.name,
                            
                        }
                        ans.append(data)                    
            
        return Response(ans,status=status.HTTP_200_OK)
    def post(self,request):
        for x in request.data:
            if(x["done"]):
                obj=get_object_or_404(toDoMaintance,id=x["id"])
                obj.done=True
                obj.save()

        return Response({"message":"done"},status=status.HTTP_200_OK)    
       


class definedlogView(APIView):
    def get(self,request):
        item_param=request.query_params.get('item')
        if(item_param is None):
            items=item.objects.all()
            ans=[]
            for x in items:
                if(x.IsItFunctioning==False):
                    continue
                if(x.MaintenanceGroup!=None):
                    print(x.MaintenanceGroup)
                    gp=get_object_or_404(maintancegp,id=x.MaintenanceGroup)
                    data={
                        "id":x.id,
                        "code":x.code,
                        "gp":gp.name,
                    }
                    ans.append(data)
            return Response(ans,status=status.HTTP_200_OK)        
        else:
            #get maintance to do for this group
            todo=toDoMaintance.objects.filter(item=item_param)
            ans=[]
            for x in todo:
                data={
                    "id":x.id,
                    "code":x.item.code,
                    "interval":x.maintanance.freq,
                    "loc_interval":x.maintanance.freq_in_loc,
                    "deadline":str(x.created_at+datetime.timedelta(days=x.maintanance.freq)).split(" ")[0],
                    "deadline_in_loc":str(x.created_at+datetime.timedelta(days=x.maintanance.freq_in_loc)).split(" ")[0],
                    "name":x.maintanance.name,
                    "done":x.done,
                }
                ans.append(data)
            items=get_object_or_404(item,id=item_param)
            final_ans={
                   "code":items.code,
                   "type":items.item_type.title,
                     "gp":get_object_or_404(maintancegp,id=items.MaintenanceGroup).name,
                     "maintanances":ans, 
            }    
            return Response(final_ans,status=status.HTTP_200_OK)