from django.shortcuts import render

# Create your views here.

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

from rest_framework.permissions import IsAuthenticated

from authen.models import User
from facilities.models import Facility
from related.models import Facilityvalidation, facilityParamDescription
from related.serializers import facilityParamDescriptionSerilizer
from settings.serializers import levelSerializer
from .models import *

from items.serializers import *
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from items.models import ItemType
from django.shortcuts import get_object_or_404
from facilities.serializers import *
from item.serializers import *
from authen.serializers import UserSerializer
import copy
import json
import pandas as pd
class gapReportView(APIView):

    def get(self,reqeust):
        pass

class exportExcel(APIView):
    def get(self,request):
        facility_Ser=facilitySerializer(Facility.objects.all(),many=True)
        facility_Ser=copy.deepcopy(facility_Ser.data)
        item_ser=itemSerializer(item.objects.all(),many=True)
        item_ser=copy.deepcopy(item_ser.data)
        country=CountryConfig.objects.all()[0]
        for x in facility_Ser:
            x['country']:country.country
            level=get_object_or_404(LevelConfig,id=x['level'])
            x['level']=level.name
            parent=Facility.objects.filter(id=x['parentid'])
            
            if(parent.count()==0):
                x['parentid']= ""
            else:    
                x['parentid']=parent[0].name
            user=get_object_or_404(User,pk=x['completerstaffname'])
            x['completerstaffname']=user.username

        for x in item_ser:
            facility=get_object_or_404(Facility,id=x['facility'])
            item_class=get_object_or_404(ItemClass,id=x['item_class'])
            item_type=get_object_or_404(ItemType,id=x['item_type'])
            x['facility']=facility.name
            x['item_class']=item_class.code
            x['item_type']=item_type.code

        # fac_json=json.dumps(facility_Ser,indent=4)
        # item_json=json.dumps(item_ser,indent=4)
        df = pd.DataFrame(facility_Ser)
        df_1 = pd.DataFrame(item_ser)
        df.to_excel('./media/exported_facility_json_data.xlsx')
        df_1.to_excel('./media/exported_item_json_data.xlsx')
        data={
            "facility":"/media/exported_facility_json_data.xlsx",
            "item":'/media/exported_item_json_data.xlsx'
        }
        return Response(data,status=status.HTTP_200_OK)


class facilitysegView(APIView):
    permission_classes=(IsAuthenticated,)

    def get(self,request):

        help=request.query_params.get('help',None)

        if (help is None):
            return Response('need query param',status=status.HTTP_400_BAD_REQUEST)

        if(help=="true"):
            user=request.user
            this_facility=Facility.objects.filter(id=user.facilityid.id)[0]
            level=this_facility.level
            allow_levels=LevelConfig.objects.filter(id__gt=level.id)
            levels=levelSerializer(allow_levels,many=True)
            power=facilityParamDescription.objects.filter(paramid=12,enabled=True)
            power=facilityParamDescriptionSerilizer(power,many=True)
            type=facilityParamDescription.objects.filter(paramid=10,enabled=True)
            type=facilityParamDescriptionSerilizer(type,many=True)
            l_data=[]
            for x in levels.data:
                data={
                    "name":x["name"],
                    "id":x["id"]
                }
                l_data.append(data)
            data={
                "level":l_data,
                "type":type.data,
                "power":power.data,

            }
            return Response(data,status=status.HTTP_200_OK)
        else:
            name=request.query_params.get('name',None)
            code=request.query_params.get('code',None)
            level=request.query_params.get('level',None)
            type=request.query_params.get('type',None)
            power=request.query_params.get('power',None)
            func=request.query_params.get('func',None)
            general_from=request.query_params.get('gfrom',None)
            general_to=request.query_params.get('gto',None)
            under_from=request.query_params.get('underfrom',None)
            under_to=request.query_params.get('underto',None)
            all_fac=Facility.objects.all()
            if(level is not None):
                all_fac=all_fac.filter(level=level)
            if(type is not None):
                all_fac=all_fac.filter(type=type)
            if(name is not None):
                all_fac=all_fac.filter(name__contains=name)
            if(code is not None):
                all_fac=all_fac.filter(code__contains=code)
        
            if(power is not None):
                all_fac=all_fac.filter(powersource=power)
            if(func is not None):
                if(func=="true"):
                    all_fac=all_fac.filter(is_functioning=True)
                else:
                    all_fac=all_fac.filter(is_functioning=False)

            if(general_from is not None):
                all_fac=all_fac.filter(populationnumber__gte=name)
            if(general_to is not None):
                all_fac=all_fac.filter(populationnumber__lte=name)
            if(under_from is not None):
                all_fac=all_fac.filter(childrennumber__gte=name)
            if(under_to is not None):
                all_fac=all_fac.filter(childrennumber__lte=name)

            ans=[]
            for x in all_fac:
                type_name=""
                power_name=""
                owner_name=""
                if(x.type != None):
                    type_name=get_object_or_404(facilityParamDescription,id=x.type).name
                if(x.powersource != None):
                    power_name=get_object_or_404(facilityParamDescription,id=x.powersource).name
                if(x.ownership != None):
                     owner_name=get_object_or_404(facilityParamDescription,id=x.ownership).name
                func="working"
               
                if(x.is_functioning != None):
                     if(not x.is_functioning):
                        func="not working"   
                
                parent=""
                if(x.parentid is not None):
                    parent=x.parentid.name
               
                data={
                    "name":x.name,
                    "parent":parent,
                    "level":x.level.id,
                    "code":x.code,
                    "type":type_name,
                    "power":power_name,
                    "owner":owner_name,
                    "func":func

                }     
                ans.append(data)
            return Response(ans,status=status.HTTP_200_OK)

class subfacView(APIView):
    permission_classes =(IsAuthenticated,)
    def get (self,request):
        
        help=request.query_params.get('help',None)

        if (help is None):
            return Response('need query param',status=status.HTTP_400_BAD_REQUEST)

        if(help=='true'):
            user=request.user
            this_facility=Facility.objects.filter(id=user.facilityid.id)[0]
            level=this_facility.level
            allow_levels=LevelConfig.objects.filter(id__gt=level.id)
            levels=levelSerializer(allow_levels,many=True)
            l_data=[]
            for x in levels.data:
                data={
                    "name":x["name"],
                    "id":x["id"]
                }
                l_data.append(data)

            return Response(l_data,status=status.HTTP_200_OK)
        else:
            #filter level
            level=request.query_params.get('level',None)
            all_fac=Facility.objects.all()
            if(level is not None):
                all_fac=Facility.objects.filter(level=level)
            #return facilityname parentname level code type power population children
            final_ans=[]
            for x in all_fac:
                parent="-"
                if(x.parentid is not None):
                    parent=x.parentid.name
                type_name=""
                power_name=""
                owner_name=""
                if(x.type != None):
                    type_name=get_object_or_404(facilityParamDescription,id=x.type).name
                data={
                    "name":x.name,
                    "parent":parent,
                    "level":x.level.id,
                    "code":x.code,
                    "type":type_name,
                    "genera;population":x.populationnumber,
                    "underage":x.childrennumber,

                }     
                final_ans.append(data)
            return Response(final_ans,status=status.HTTP_200_OK)    



                 
class facilitymap(APIView):
    permission_classes=(IsAuthenticated,)

    def get(self,request):

        help=request.query_params.get('help',None)

        if (help is None):
            return Response('need query param',status=status.HTTP_400_BAD_REQUEST)

        if(help=="true"):
            user=request.user
            this_facility=Facility.objects.filter(id=user.facilityid.id)[0]
            level=this_facility.level
            allow_levels=LevelConfig.objects.filter(id__gt=level.id)
            levels=levelSerializer(allow_levels,many=True)
            power=facilityParamDescription.objects.filter(paramid=12,enabled=True)
            power=facilityParamDescriptionSerilizer(power,many=True)
            type=facilityParamDescription.objects.filter(paramid=10,enabled=True)
            type=facilityParamDescriptionSerilizer(type,many=True)
            l_data=[]
            for x in levels.data:
                data={
                    "name":x["name"],
                    "id":x["id"]
                }
                l_data.append(data)
            data={
                "level":l_data,
                "type":type.data,
                "power":power.data,

            }
            return Response(data,status=status.HTTP_200_OK)
        else:
            level=request.query_params.get('level',None)
            type=request.query_params.get('type',None)
            power=request.query_params.get('power',None)
            func=request.query_params.get('func',None)
            all_fac=Facility.objects.all()
            if(level is not None):
                all_fac=all_fac.filter(level=level)
            if(type is not None):
                all_fac=all_fac.filter(type=type)
        
            if(power is not None):
                all_fac=all_fac.filter(powersource=power)
            if(func is not None):
                if(func=="true"):
                    all_fac=all_fac.filter(is_functioning=True)
                else:
                    all_fac=all_fac.filter(is_functioning=False)


            ans=[]
            for x in all_fac:
                data={
                    "cordinates":x.gpsCordinate
                }
                ans.append(data)
            return Response(ans,status=status.HTTP_200_OK)

 
                


            
        
