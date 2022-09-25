from decimal import Decimal
from sqlite3 import Date
from time import timezone

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
from PQS.models import pqs3,pqs4
from PQS.serializers import *
from authen.models import User
from facilities.models import Facility
from related.models import Facilityvalidation, facilityParamDescription, itemParamDescription
from related.serializers import facilityParamDescriptionSerilizer,itemParamDescriptionSerilizer
from settings.serializers import levelSerializer
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
from facilities.serializers import *
from item.serializers import *
from item.models import item
from authen.serializers import UserSerializer
import copy
import json
import pandas as pd
import os
import datetime
from related.models import *
from related.serializers import *
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
        rel_fac=relatedFacility.objects.all()
        rel_item=Field.objects.all()
        for x in facility_Ser:
            
            
            for z in rel_fac:
                strs=z.state
                if(x[strs] != None):
                    param=facilityParam.objects.filter(fieldid=z.id).order_by('order')
                    if(param.count()!=0):
                        desc=facilityParamDescription.objects.filter(id=x[strs]).order_by('order')
                        if(desc.count()!=0):
                            x[strs]=desc[0].name


            x["created_at"]=x["created_at"].split("T")[0]
            x["updated_at"]=x["updated_at"].split("T")[0]
            x['country']=country.country
            level=get_object_or_404(LevelConfig,id=x['level'])
            x['level']=str(level.id)+"-" +level.name
            parent=Facility.objects.filter(id=x['parentid'])
            
            if(parent.count()==0):
                x['parentid']= ""
            else:    
                x['parentid']=parent[0].name
            try:    
                user=get_object_or_404(User,pk=x['completerstaffname'])
                x['completerstaffname']=user.username
            except:
                x['completerstaffname']=""

        for x in item_ser:
            for z in rel_item:
                strs=z.state
                if(x[strs] != None):
                    param=itemParam.objects.filter(fieldid=z.id).order_by('order')
                    if(param.count()!=0):
                        print(x[strs])
                        desc=itemParamDescription.objects.filter(id=x[strs])
                        print(desc)
                        print(x[strs])
                        if(desc.count()!=0):
                            x[strs]=desc[0].name
                            
                            
            try:
                facility=get_object_or_404(Facility,id=x['facility'])
                item_class=get_object_or_404(ItemClass,id=x['item_class'])
                item_type=get_object_or_404(ItemType,id=x['item_type'])
                x['facility']=facility.name
                x['item_class']=item_class.code
                x['item_type']=item_type.code
            except:
                x['facility']=""
                x['item_class']=""
                x['item_type']=""
            if(x['Manufacturer'] !=None):
                x['Manufacturer']=Manufacturer.objects.filter(id=x['Manufacturer'])[0].describe
            x["created_at"]=x["created_at"].split("T")[0]
            x["updated_at"]=x["updated_at"].split("T")[0]
                    

        # fac_json=json.dumps(facility_Ser,indent=4)
        # item_json=json.dumps(item_ser,indent=4)
        df = pd.DataFrame(facility_Ser)
        df_1 = pd.DataFrame(item_ser)
        facility_str=country.codecountry+str(datetime.datetime.now()).split(".")[0]+"-Facility.xlsx"
        item_str=country.codecountry+str(datetime.datetime.now()).split(".")[0]+"-Item.xlsx"
        df.to_excel('./media/'+facility_str)
        df_1.to_excel('./media/'+item_str)
        data={
            "facility":"/media/"+facility_str,
            "item":'/media/'+item_str
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
            allow_levels=LevelConfig.objects.filter(id__gte=level.id)
            counter=CountryConfig.objects.all()[0]
            allow_levels=allow_levels.filter(id__lte=counter.levels) 
            levels=levelSerializer(allow_levels,many=True)
            power=facilityParamDescription.objects.filter(paramid=10,enabled=True)
            power=facilityParamDescriptionSerilizer(power,many=True)
            type=facilityParamDescription.objects.filter(paramid=12,enabled=True)
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
            all_fac=Facility.objects.filter(parentid=request.user.facilityid.id,is_deleted=False)
            all_fac=Facility.objects.filter(id=request.user.facilityid.id)|all_fac
            if(level is not None and level !="-1"):
                all_fac=all_fac.filter(level=level)
            if(type is not None and type!="-1"):
                all_fac=all_fac.filter(type=type)
            if(name is not None):
                all_fac=all_fac.filter(name__icontains=name)
            if(code is not None):
                all_fac=all_fac.filter(code__icontains=code)
        
            if(power is not None and power!="-1"):
                all_fac=all_fac.filter(powersource=power)
            if(func is not None and func!="-1"):
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
            allow_levels=LevelConfig.objects.filter(id__gte=level.id)
            counter=CountryConfig.objects.all()[0]
            allow_levels=allow_levels.filter(id__lte=counter.levels)
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
            all_fac=Facility.objects.filter(parentid=request.user.facilityid.id,is_deleted=False)
            all_fac=Facility.objects.filter(id=request.user.facilityid.id)|all_fac
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
                    "generalpopulation":x.populationnumber,
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
            allow_levels=LevelConfig.objects.filter(id__gte=level.id)
            counter=CountryConfig.objects.all()[0]
            allow_levels=allow_levels.filter(id__lte=counter.levels)
            levels=levelSerializer(allow_levels,many=True)
            power=facilityParamDescription.objects.filter(paramid=10,enabled=True)
            power=facilityParamDescriptionSerilizer(power,many=True)
            type=facilityParamDescription.objects.filter(paramid=12,enabled=True)
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
            all_fac=Facility.objects.filter(parentid=request.user.facilityid.id,is_deleted=False)
            all_fac=Facility.objects.filter(id=request.user.facilityid.id)|all_fac
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
                try:
                    if(x.gpsCordinate is not None):
                        print(x.gpsCordinate)
                        lat=float(x.gpsCordinate.split(",")[0].split("(")[1])
                        lang=float(x.gpsCordinate.split(",")[1].split(")")[0])
                        data={
                            "cordinates": [lat,lang]
                        }
                        ans.append(data)
                except:
                    continue        
            return Response(ans,status=status.HTTP_200_OK)

#item grouped report
# have facility filter and item options
class itemGroupedReport(APIView):
    permission_classes=(IsAuthenticated,)
    def get(self,request):
        help=request.query_params.get('help',None)
        if(help is None):
            return Response('need query param',status=status.HTTP_400_BAD_REQUEST)

        if(help=="true"):
            user=request.user
            this_facility=Facility.objects.filter(id=user.facilityid.id)[0]
            level=this_facility.level
            allow_levels=LevelConfig.objects.filter(id__gte=level.id)
            counter=CountryConfig.objects.all()[0]
            allow_levels=allow_levels.filter(id__lte=counter.levels)
            levels=levelSerializer(allow_levels,many=True)
            power=facilityParamDescription.objects.filter(paramid=10,enabled=True)
            powerss=facilityParamDescriptionSerilizer(power,many=True)
            type=facilityParamDescription.objects.filter(paramid=12,enabled=True)
            typess=facilityParamDescriptionSerilizer(type,many=True)
            l_data=[]

            for x in levels.data:
                data={
                    "name":x["name"],
                    "id":x["id"]
                }
                l_data.append(data)
            #filter item class and item type by active
            # item class
            item_class=ItemClass.objects.filter(active=True)
            items=[]
            for x in item_class:
                item_type=ItemType.objects.filter(itemclass=x.id,active=True)
                types=[]
                for y in item_type:
                    data_item={
                        "name":y.title,
                        "id":y.id
                    }
                    types.append(data_item)
                manufac=Manufacturer.objects.filter(itemclass=x.id,active=True)    
                manufacturers=[]
                for y in manufac:
                    data_item={
                        "name":y.describe,
                        "id":y.id
                    }
                    manufacturers.append(data_item)
                data={
                    "item_class_name":x.title,
                    "item_class_id":x.id,
                    "item_type":types,
                    "manufacturer":manufacturers
                }
                items.append(data)
            physcal=itemParamDescription.objects.filter(paramid=9,enabled=True)
            physcal=itemParamDescriptionSerilizer(physcal,many=True) 
            working=itemParamDescription.objects.filter(paramid=11,enabled=True)
            working=itemParamDescriptionSerilizer(working,many=True)
            financial=itemParamDescription.objects.filter(paramid=14,enabled=True)
            financial=itemParamDescriptionSerilizer(financial,many=True)
            powers=itemParamDescription.objects.filter(paramid=12,enabled=True)
            powers=itemParamDescriptionSerilizer(powers,many=True)   

            datas={
                "level":l_data,
                "type":typess.data,
                "power":powerss.data,
                "item":items,
                "physical":physcal.data,
                "financial":financial.data,
                "working":working.data,
                "item_power":powers.data,
            }
            return Response(datas,status=status.HTTP_200_OK)
        else:
            name=request.query_params.get('name',None)
            level=request.query_params.get('level',None)
            type=request.query_params.get('type',None)
            power=request.query_params.get('power',None)
            code=request.query_params.get('code',None)
            item_class=request.query_params.get('item_class',None)
            item_type=request.query_params.get('item_type',None)
            physical=request.query_params.get('physical',None)
            financial=request.query_params.get('financial',None)
            working=request.query_params.get('working',None)
            item_power=request.query_params.get('item_power',None)
            manufacturer=request.query_params.get('manufacturer',None)
            pqs=request.query_params.get('pqs',None)
            year_from=request.query_params.get('year_from',None)
            year_to=request.query_params.get('year_to',None)
            capacity_from=request.query_params.get('capacity_from',None)
            capacity_to=request.query_params.get('capacity_to',None)
            items=item.objects.all()
            facility=Facility.objects.filter(parentid=request.user.facilityid.id,is_deleted=False)
            facility=Facility.objects.filter(id=request.user.facilityid.id)|facility
            if(name is not None):
                facility=Facility.objects.filter(name__icontains=name)
            if(level is not None):
                facility=facility.filter(level=level)
            if(type is not None):
                facility=facility.filter(type=type)
            if(power is not None):
                facility=facility.filter(powersource=power)
            if(code is not None):
                facility=facility.filter(code__icontains=code)
            if(item_class is not None):
                items=items.filter(item_class=item_class)
            if(item_type is not None):
                items=items.filter(item_type=item_type)
            if(physical is not None):
                items=items.filter(PhysicalConditions=physical)
            if(financial is not None):
                items=items.filter(FinancialSource=financial)
            if(working is not None):
                items=items.filter(WorkingConditions=working)
            if(item_power is not None):
                items=items.filter(power=item_power)
            if(manufacturer is not None):
                items=items.filter(manufacturer=manufacturer)
            if(pqs is not None):
                items=items.filter(PQSPISCode__icontains=pqs)
            if(year_from is not None):
                items=items.filter(YearInstalled__gte=year_from)
            if(year_to is not None):
                items=items.filter(YearInstalled__lte=year_to)
            if(capacity_from is not None):
                items=items.filter(FreezerNetCapacity__gte=capacity_from)
            if(capacity_to is not None):
                items=items.filter(FreezerNetCapacity__lte=capacity_to)
            fac_id=[]
            for x in facility:
                fac_id.append(x.id)    
            #all facilitys contain same item
            items=items.filter(facility__in=fac_id)
            same_type=[]
            same_pqs=[]
            same_manufacturer=[]
            same_model=[]
            for x in items:
                if x.item_type not in same_type:
                    same_type.append(x.item_type)
                if x.PQSPISCode not in same_pqs:
                    same_pqs.append(x.PQSPISCode)
                if x.Manufacturer not in same_manufacturer:
                    same_manufacturer.append(x.Manufacturer)
                if x.Model not in same_model:
                    same_model.append(x.Model)
            final_answer=[]
            for x in same_type:
                new_items=items.filter(item_type=x)
                for y in same_model:
                    new_items=new_items.filter(Model=y)
                    for z in same_manufacturer:
                        new_items=new_items.filter(Manufacturer=z)
                        for w in same_pqs:
                            new_items=new_items.filter(PQSPISCode=w) 
                            fac_list=[]
                            added_fac=[]
                            for a in new_items:
                                facility=get_object_or_404(Facility,id=a.facility.id)
                                data={
                                    "name":facility.name,
                                    "id":facility.id,
                                }
                                if(facility.id not in added_fac):
                                    added_fac.append(facility.id)
                                    fac_list.append(data)
                            manufac=""
                            count=new_items.count()        
                            if(z is not None):
                                manufac=Manufacturer.objects.filter(id=z)
                                if(manufac.count()>0):
                                    manufac=manufac[0].describe
       
                            final_answer.append({"item_type":x.title,"model":y,"manufacturer":manufac,"pqs":w,"facility":fac_list,"count":count})
            return Response(final_answer,status=status.HTTP_200_OK)                    

class itemFacilityReport(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self,request):
        # get help query param and check none
        help=request.query_params.get('help',None)
        if(help is  None):
            return Response("need query param",status=status.HTTP_400_BAD_REQUEST)

        # check if help is "true"
        # if help is "true" return level poweer source type for facility and item_class ,item_type,physical,financial,working,item_power
        # if help is "false" return items filter by query params
        if(help=="true"):
            user=request.user
            this_facility=Facility.objects.filter(id=user.facilityid.id)[0]
            level=this_facility.level
            allow_levels=LevelConfig.objects.filter(id__gte=level.id)
            counter=CountryConfig.objects.all()[0]
            allow_levels=allow_levels.filter(id__lte=counter.levels)
            levels=levelSerializer(allow_levels,many=True)
            power=facilityParamDescription.objects.filter(paramid=10,enabled=True)
            powerss=facilityParamDescriptionSerilizer(power,many=True)
            type=facilityParamDescription.objects.filter(paramid=12,enabled=True)
            typess=facilityParamDescriptionSerilizer(type,many=True)
            l_data=[]

            for x in levels.data:
                data={
                    "name":x["name"],
                    "id":x["id"]
                }
                l_data.append(data)
            item_class=ItemClass.objects.filter(active=True)
            items=[]
            for x in item_class:
                item_type=ItemType.objects.filter(itemclass=x.id,active=True)
                types=[]
                for y in item_type:
                    data_item={
                        "name":y.title,
                        "id":y.id
                    }
                    types.append(data_item)
                data={
                    "item_class_name":x.title,
                    "item_class_id":x.id,
                    "item_type":types,
                }
                items.append(data)
            physcal=itemParamDescription.objects.filter(paramid=9,enabled=True)
            physcal=itemParamDescriptionSerilizer(physcal,many=True) 
            working=itemParamDescription.objects.filter(paramid=11,enabled=True)
            working=itemParamDescriptionSerilizer(working,many=True)
            financial=itemParamDescription.objects.filter(paramid=14,enabled=True)
            financial=itemParamDescriptionSerilizer(financial,many=True)
            powers=itemParamDescription.objects.filter(paramid=10,enabled=True)
            powers=itemParamDescriptionSerilizer(powers,many=True)   

            datas={
                "level":l_data,
                "type":typess.data,
                "power":powerss.data,
                "item":items,
                "physical":physcal.data,
                "financial":financial.data,
                "working":working.data,
                "item_power":powers.data,
            }
            return Response(datas,status=status.HTTP_200_OK)    
        else:
            name=request.query_params.get('name',None)
            level=request.query_params.get('level',None)
            type=request.query_params.get('type',None)
            power=request.query_params.get('power',None)
            code=request.query_params.get('code',None)
            item_class=request.query_params.get('item_class',None)
            item_type=request.query_params.get('item_type',None)
            physical=request.query_params.get('physical',None)
            financial=request.query_params.get('financial',None)
            working=request.query_params.get('working',None)
            item_power=request.query_params.get('item_power',None)
            items=item.objects.all()
            facility=Facility.objects.filter(parentid=request.user.facilityid.id,is_deleted=False)
            facility=Facility.objects.filter(id=request.user.facilityid.id)|facility
            if(name is not None):
                facility=facility.filter(name__icontains=name)
            if(level is not None):
                facility=facility.filter(level=level)
            if(type is not None):
                facility=facility.filter(type=type)
            if(power is not None):
                facility=facility.filter(powersource=power)
            if(code is not None):
                facility=facility.filter(code__icontains=code)
            if(item_class is not None):
                items=items.filter(item_class=item_class)
            if(item_type is not None):
                items=items.filter(item_type=item_type)
            if(physical is not None):
                items=items.filter(PhysicalConditions=physical)
            if(financial is not None):
                items=items.filter(FinancialSource=financial)
            if(working is not None):
                items=items.filter(WorkingConditions=working)
            if(item_power is not None):
                items=items.filter(power=item_power)
            fac_id=[]
            for x in facility:
                fac_id.append(x.id)
            items=items.filter(facility__in=fac_id)
            final_answer=[]
            for x in items:
                facility=x.facility
                parent="Central store"
                if(facility.parentid is not None):
                    parent=facility.parentid.name
                level=facility.level.id
                type_name=""
                if(facility.type is not None):
                    type_name=get_object_or_404(facilityParamDescription,id=x.facility.type).name
                fac_data={
                    "fac_name":facility.name,
                    "fac_parent":parent,
                    "fac_level":level,
                    "fac_type":type_name,

                }
                item_class=x.item_class.title
                item_type=x.item_type.title
                code=x.code
                pqs=x.PQSPISCode
                model=x.Model
                manufac=x.Manufacturer
                if(manufac is not None):
                    manufac=Manufacturer.objects.filter(id=manufac)[0].describe
                capacity=x.FreezerNetCapacity
                year=x.YearInstalled
                physical=""
                if(x.PhysicalConditions is not None):
                    physical=x.PhysicalConditions
                    physical=get_object_or_404(itemParamDescription,id=physical).name
                financial=""
                if(x.FinancialSource is not None):
                    financial=x.FinancialSource
                    financial=get_object_or_404(itemParamDescription,id=financial).name
                power=""
                if(x.EnergySource is not None):
                    power=get_object_or_404(itemParamDescription,id=x.EnergySource).name
                working=""
                if(x.WorkingConditions is not None):
                    working=x.WorkingConditions
                    working=get_object_or_404(itemParamDescription,id=working).name
                func="NO"
                if(x.IsItFunctioning):
                    func="Yes"
                financ=""
    
                item_data={
                    "item_class":item_class,
                    "item_type":item_type,
                    "code":code,
                    "pqs":pqs,
                    "model":model,
                    "manufac":manufac,
                    "capacity":capacity,
                    "year":year,
                    "physical":physical,
                    "financial":financial,
                    "power":power,
                    "working":working,
                    "func":func,
                }
                data={
                    "facility":fac_data,
                    "item":item_data
                }
                final_answer.append(data)
            return Response(final_answer,status=status.HTTP_200_OK)    

class facilityProfileView(APIView):
    permission_classes =(IsAuthenticated,)
    def get(self,request):
        user=request.user
        this_facility=Facility.objects.filter(id=user.facilityid.id)[0]
        level=this_facility.level
        allow_levels=LevelConfig.objects.filter(id__gt=level.id)
        counter=CountryConfig.objects.all()[0]
        allow_levels=allow_levels.filter(id__lte=counter.levels)
        by_type=[]
        by_owner=[]
        by_power=[]
        general_1=[]
        under_11=[]
        type=facilityParamDescription.objects.filter(paramid=12,enabled=True)
        owner=facilityParamDescription.objects.filter(paramid=5,enabled=True)
        power=facilityParamDescription.objects.filter(paramid=10,enabled=True)
        for x in allow_levels:
            facility=Facility.objects.filter(parentid=request.user.facilityid.id,is_deleted=False)
            facility=Facility.objects.filter(id=request.user.facilityid.id)|facility
            facility=facility.filter(level=x.id)
            
            for y in type:
                count=facility.filter(type=y.id).count()
                data={
                    "level":x.id,
                    "name":x.name,
                    "type":y.name,
                    "count":count
                }
                by_type.append(data)
            data={
                "level":x.id,
                "name":x.name,
                "type":"--",
                "count":facility.filter(type=None).count()
            }
            by_type.append(data)
            for y in owner:
                count=facility.filter(ownership=y.id).count()
                data={
                    "level":x.id,
                    "name":x.name,
                    "owner":y.name,
                    "count":count
                }
                by_owner.append(data)
            data={
                "level":x.id,
                "name":x.name,
                "owner":"--",
                "count":facility.filter(ownership=None).count()
            }
            by_owner.append(data)
            for y in power:
                count=facility.filter(powersource=y.id).count()
                data={
                    "level":x.id,
                    "name":x.name,
                    "power":y.name,
                    "count":count
                }
                by_power.append(data)
            data={
                "level":x.id,
                "name":x.name,
                "power":"--",
                "count":facility.filter(powersource=None).count()
            }
            by_power.append(data)
            sumg=0
            sum1=0
            min=10000000000000000
            max=-1
            min1=10000000000000000
            max1=-1
            for y in facility:
                general=0
                under_1=0
                if(y.populationnumber is not None):
                    general=y.populationnumber
                if(y.childrennumber is not None):
                    under_1=y.childrennumber
                sumg+=general
                sum1+=under_1
                if(general<min):
                    min=general
                if(general>max):
                    max=general
                if(under_1<min1):
                    min1=under_1
                if(under_1>max1):
                    max1=under_1
            avgg=1        
            if(facility.count()>0):
                avgg=sumg/facility.count()     
            if (min==10000000000000000):
                min=0
            if (max==-1):
                max=0
            if (min1==10000000000000000):
                min1=0
            if (max1==-1):
                max1=0  
            data={
                "level":x.id,
                "name":x.name,
                "total":sumg,
                "min":min,
                "max":max,
                "avg":avgg
            }
            general_1.append(data)
            avg1=1
            if(facility.count()>0):
                avg1=sum1/facility.count()
            data1={
                "level":x.id,
                "name":x.name,
                "total":sum1,
                "min":min1,
                "max":max1,
                "avg":avg1
            }
            under_11.append(data1)
        final_answer={
            "by_type":by_type,
            "by_owner":by_owner,
            "by_power":by_power,
            "general":general_1,
            "under_1":under_11
        }
        return Response(final_answer,status=status.HTTP_200_OK)
                                   
class profileColdchainView(APIView):
        permission_classes=(IsAuthenticated,)
        def get(self,request):
            degree=request.query_params.get('degree',None) 
            if(degree is None):
                return Response("Please provide a degree",status=status.HTTP_400_BAD_REQUEST)
            user=request.user
            this_facility=Facility.objects.filter(id=user.facilityid.id)[0]
            level=this_facility.level
            allow_levels=LevelConfig.objects.filter(id__gte=level.id)
            counter=CountryConfig.objects.all()[0]
            allow_levels=allow_levels.filter(id__lte=counter.levels) 
            ans_1=[]
            table_1=[]
            table_2=[]
            for x in allow_levels:
                facility=Facility.objects.filter(parentid=request.user.facilityid.id,is_deleted=False)
                facility=Facility.objects.filter(id=request.user.facilityid.id)|facility
                facility=facility.filter(level=x.id)
                general=0
                under1=0
                cold_a=0
                nw_cold_a=0

                freezer=0
                nw_freezer=0
                refig=0
                nw_refrig=0
                fr=0
                nw_fr=0
                cb=0
                nw_cb=0
                vc=0
                nw_vc=0
                available=0
                
                for y in facility:
                    if(y.populationnumber is not None):
                        general+=y.populationnumber
                    if(y.childrennumber is not None):
                        under1+=y.childrennumber
                    items=item.objects.filter(facility=y.id,isDel=False)
                    for z in items:
                        if(z.item_type.id==1):
                            if(z.IsItFunctioning==True):
                                cold_a+=1
                            else:
                                nw_cold_a+=1
                        if(z.item_type.id==2):
                            if(z.IsItFunctioning==True):
                                freezer+=1
                            else:
                                nw_freezer+=1
                        if(z.item_type.id==3):
                            if(z.IsItFunctioning==True):
                                refig+=1
                            else:
                                nw_refrig+=1
                        if(z.item_type.id==4):
                            if(z.IsItFunctioning==True):
                                fr+=1
                            else:
                                nw_fr+=1
                        if(z.item_type.id==5):
                            if(z.IsItFunctioning==True):
                                cb+=1
                            else:
                                nw_cb+=1
                        if(z.item_type.id==6):
                            if(z.IsItFunctioning==True):
                                vc+=1
                            else:
                                nw_vc+=1
                        if(degree=="4"):
                            if(z.StorageCondition=="1"):
                                available+=z.NetVaccineStorageCapacity
                        if(degree=="1"):
                            if(z.StorageCondition=="2"):
                                available+=z.NetVaccineStorageCapacity  
                        if(degree=="2"):
                            if(z.StorageCondition=="3"):
                                available+=z.NetVaccineStorageCapacity
                        if(degree=="3"):
                            if(z.StorageCondition=="4"):
                                available+=z.NetVaccineStorageCapacity  
                country=CountryConfig.objects.all()[0]
                req=0
                if(degree=="1"):
                    req=x.uppervol
                if(degree=="2"):
                    req=x.undervol
                if(degree=="3"):
                    req=x.m70vol
                if(degree=="4"):
                    req=x.m25vol
                require_capacity=1
                available_capacity=1    
                if(country.poptarget=='General population'):
                    if(req is not None):
                        require_capacity=general*req
                        available_capacity=general*available
                else:
                    if(req is not None):
                        require_capacity=under1*req
                        available_capacity=under1*available        
                data1={
                    "id":x.id,
                    "name":x.name,
                    "general":general,
                    "under1":under1,
                    "req":req,
                    "available":available,
                    "diff":float(available)-float(req),
                    "require_capacity":require_capacity/1000,
                    "available_capacity":available_capacity/1000,
                    "diff_capacity":(float(available_capacity)-float(require_capacity))/1000,
                }
                table_2.append(data1)

                data={
                    "id":x.id,
                    "name":x.name,
                    "general":general,
                    "under1":under1,
                    "cold_a":cold_a,
                    "nw_cold_a":nw_cold_a,
                    "freezer":freezer,
                    "nw_freezer":nw_freezer,
                    "refrig":refig,
                    "nw_refrig":nw_refrig,
                    "fr":fr,
                    "nw_fr":nw_fr,
                    "cb":cb,
                    "nw_cb":nw_cb,
                    "vc":vc,
                    "nw_vc":nw_vc

                }   
                table_1.append(data)
            ans={
                "table_1":table_1,
                "table_2":table_2

            }  
            return Response(ans,status=status.HTTP_200_OK)  


class gapItemReportView(APIView):
      permission_classes=(IsAuthenticated,)
      def get(self,request):
        help=request.query_params.get('help',None)
        if(help is None):
            return Response("Please provide help",status=status.HTTP_400_BAD_REQUEST)

        if(help=="true"):
            user=request.user
            this_facility=Facility.objects.filter(id=user.facilityid.id)[0]
            level=this_facility.level
            allow_levels=LevelConfig.objects.filter(id__gte=level.id)
            counter=CountryConfig.objects.all()[0]
            allow_levels=allow_levels.filter(id__lte=counter.levels)
            levels=levelSerializer(allow_levels,many=True)
            power=facilityParamDescription.objects.filter(paramid=10,enabled=True)
            powerss=facilityParamDescriptionSerilizer(power,many=True)
            type=facilityParamDescription.objects.filter(paramid=12,enabled=True)
            typess=facilityParamDescriptionSerilizer(type,many=True)
            l_data=[]

            for x in levels.data:
                data={
                    "name":x["name"],
                    "id":x["id"]
                }
                l_data.append(data)
            datas={
                "level":l_data,
                "type":typess.data,
                "power":powerss.data,
            }
            return Response(datas,status=status.HTTP_200_OK) 
        else:
            gapSave.objects.all().delete()
            name=request.query_params.get('name',None)
            level=request.query_params.get('level',None)
            type=request.query_params.get('type',None)
            power=request.query_params.get('power',None)
            code=request.query_params.get('code',None)
            degree=request.query_params.get('degree',None)
            option=request.query_params.get('option',None)
            year_from=request.query_params.get('year_from',None)
            year_to=request.query_params.get('year_to',None)
            calculate_for=request.query_params.get('calculate_for',None)
            cc_for=calculate_for
            if(calculate_for is not  None):
                calculate_for=int(calculate_for)
                current=datetime.date.today().year
                calculate_for=calculate_for-current
            
            facility=Facility.objects.filter(parentid=request.user.facilityid.id,is_deleted=False)
            facility=Facility.objects.filter(id=request.user.facilityid.id)|facility
            items=item.objects.all()
            if(degree is None):
                return Response("degree is required",status.HTTP_200_OK)
            if(name is not None):
                facility=facility.filter(name__icontains=name)
            if(level is not None):
                facility=facility.filter(level=level)
            if(type is not None):
                facility=facility.filter(type=type)
            if(power is not None):
                facility=facility.filter(powersource=power)
            if(code is not None):
                facility=facility.filter(code__icontains=code)
            if(option=="2"):
                items=items.exclude(PQSPISCode=None)
            if(option=="3"):
                if(year_from is not None):
                    items=items.filter(YearInstalled__gte=year_from)
                if(year_to is not None):
                    items=items.filter(YearInstalled__lte=year_to)
            ans=[]
            for x in facility:
                capacity1=0
                fcapacity1=0
                capacity2=0
                fcapacity2=0
                capacity3=0
                fcapacity3=0
                capacity4=0
                fcapacity4=0
                capacity5=0
                fcapacity5=0

                items=item.objects.filter(facility=x.id,isDel=False)
                for y in items:
                    if(degree=="1"):
                        if(y.StorageCondition=="2"):
                            capacity1+=y.NetVaccineStorageCapacity
                            if(y.IsItFunctioning):
                                fcapacity1+=y.NetVaccineStorageCapacity
                    if(degree=="2"):
                        if(y.StorageCondition=="3"):
                            capacity2+=y.NetVaccineStorageCapacity
                            if(y.IsItFunctioning):
                                fcapacity2+=y.NetVaccineStorageCapacity
                    if(degree=="3"):
                        if(y.StorageCondition=="4"):
                            capacity3+=y.NetVaccineStorageCapacity
                            if(y.IsItFunctioning):
                                fcapacity3+=y.NetVaccineStorageCapacity
                    if(degree=="4"):
                        if(y.StorageCondition=="1"):
                            capacity4+=y.NetVaccineStorageCapacity
                            if(y.IsItFunctioning):
                                fcapacity4+=y.NetVaccineStorageCapacity
                    if(degree=="5"):
                        if(y.StorageCondition=="5"):
                            capacity5+=y.NetVaccineStorageCapacity
                            if(y.IsItFunctioning):
                                fcapacity5+=y.NetVaccineStorageCapacity    
                country=CountryConfig.objects.all()[0]
                req1=1
                req2=1
                req3=1
                req4=1
                req5=1
                pop=0
                if(country.poptarget=='General population'):
                    if(x.populationnumber is not None):
                        pop=x.populationnumber
                else:
                    if(x.childrennumber is not None):
                        pop=x.childrennumber
                if(calculate_for==0 or calculate_for is None):
                    req1=pop*x.level.uppervol/1000
                    req2=pop*x.level.undervol/1000
                    req3=pop*x.level.m70vol/1000
                    req4=pop*x.level.m25vol/1000
                    req5=pop*x.level.dryvol/1000
                else:
                    calculate_for=(country.poprate)**calculate_for
                    req1=pop*x.level.uppervolnew/1000*calculate_for
                    req2=pop*x.level.undervolnew/1000*calculate_for
                    req3=pop*x.level.m70volnew/1000*calculate_for
                    req4=pop*x.level.m25volnew/1000*calculate_for
                    req5=pop*x.level.dryvolnew/1000*calculate_for
                    
                excees1=False
                excees2=False
                excees3=False
                excees4=False
                excees5=False
                req1=float(req1)
                req2=float(req2)
                req3=float(req3)
                req4=float(req4)
                req5=float(req5)

                # fcapacity1=Decimal(fcapacity1)
                # fcapacity2=Decimal(fcapacity2)
                # fcapacity3=Decimal(fcapacity3)
                # fcapacity4=Decimal(fcapacity4)
                # fcapacity5=Decimal(fcapacity5)
                if(req1-fcapacity1<0):
                    excees1=True
                if(req2-fcapacity2<0):
                    excees2=True
                if(req3-fcapacity3<0):
                    excees3=True
                if(req4-fcapacity4<0):
                    excees4=True
                if(req5-fcapacity5<0):
                    excees5=True
                type_name="--"
                if(x.type != None):
                    type_name=get_object_or_404(facilityParamDescription,id=x.type).name

                data={}  
                parentName="--"
                if(x.parentid is not None):
                    parentName=x.parentid.name  
                if(degree=="6"):
                    data={
                    "id":x.id,
                    "name":x.name,
                    "code":x.code ,
                    "level":x.level.name,
                    "parent":parentName,
                    "general":x.populationnumber,
                    "children":x.childrennumber,
                    "type":type_name,
                    "tcapacity1":capacity1,
                    "tcapacity2":capacity2,
                    "tcapacity3":capacity3,
                    "tcapacity4":capacity4,
                    "tcapacity5":capacity5,
                    "fcapacity1":capacity1,
                    "fcapacity2":capacity2,
                    "fcapacity3":capacity3,
                    "fcapacity4":capacity4,
                    "fcapacity5":capacity5,
                    "req1":req1,
                    "req2":req2,
                    "req3":req3,
                    "req4":req4,
                    "req5":req5,
                    "excees1":fcapacity1-req1,
                    "excees2":fcapacity2-req2,
                    "excees3":fcapacity3-req3,
                    "excees4":fcapacity4-req4,
                    "excees5":fcapacity5-req5,
                    "exceed1":excees1,
                    "exceed2":excees2,
                    "exceed3":excees3,
                    "exceed4":excees4,
                    "exceed5":excees5,

                }
                else:
                    data={
                    "id":x.id,
                    "name":x.name,
                    "code":x.code ,
                    "level":x.level.name,
                    "parent":parentName,
                    "general":x.populationnumber,
                    "children":x.childrennumber,
                    "type":type_name
                }
                    if(degree=="1"):
                        data["tcapacity1"]=capacity1
                        data["fcapacity1"]=fcapacity1
                        data["req1"]=req1
                        data["excees1"]=fcapacity1-req1
                        data["exceed1"]=excees1
                    if(degree=="2"):
                        data["tcapacity1"]=capacity2
                        data["fcapacity1"]=fcapacity2
                        data["req1"]=req2
                        data["excees1"]=fcapacity2-req2
                        data["exceed1"]=excees2
                    if(degree=="3"):
                        data["tcapacity1"]=capacity3
                        data["fcapacity1"]=fcapacity3
                        data["req1"]=req3
                        data["excees1"]=fcapacity3-req3
                        data["exceed1"]=excees3
                    if(degree=="4"):                        
                        data["tcapacity1"]=capacity4
                        data["fcapacity1"]=fcapacity4
                        data["req1"]=req4
                        data["excees1"]=fcapacity4-req4
                        data["exceed1"]=excees4
                    if(degree=="5"):
                        data["tcapacity1"]=capacity5
                        data["fcapacity1"]=fcapacity5
                        data["req1"]=req5
                        data["excees1"]=fcapacity5-req5
                        data["exceed1"]=excees5
                save_arr=[]                
                parent_save=None
                if(x.parentid is not None):
                    parent_save=x.parentid.id           
                save_data1={
                    "facility":x.id,
                    "parent_fac":parent_save,
                    "level":x.level.id,
                    "code":x.code,
                    "condition":1,
                    "req_capacity":req1,
                    "available":capacity1,
                    "func_cap":fcapacity1,
                    "exces":fcapacity1-req1,
                    "general":x.populationnumber,
                    "under_1":x.childrennumber,
                    "calculate_for":cc_for
                }
                save_arr.append(save_data1)
                save_data2={
                    "facility":x.id,
                    "parent_fac":parent_save,
                    "level":x.level.id,
                    "code":x.code,
                    "condition":2,
                    "req_capacity":req2,
                    "available":capacity2,
                    "func_cap":fcapacity2,
                    "exces":fcapacity2-req2,
                    "general":x.populationnumber,
                    "under_1":x.childrennumber,
                    "calculate_for":cc_for

                }
                save_arr.append(save_data2)
                save_data3={
                    "facility":x.id,
                    "parent_fac":parent_save,
                    "level":x.level.id,
                    "code":x.code,
                    "condition":3,
                    "req_capacity":req3,
                    "available":capacity3,
                    "func_cap":fcapacity3,
                    "exces":fcapacity3-req3,
                    "general":x.populationnumber,
                    "under_1":x.childrennumber,
                    "calculate_for":cc_for

                }
                save_arr.append(save_data3)
                save_data4={
                    "facility":x.id,
                    "parent_fac":parent_save,
                    "level":x.level.id,
                    "code":x.code,
                    "condition":4,
                    "req_capacity":req4,
                    "available":capacity4,
                    "func_cap":fcapacity4,
                    "exces":fcapacity4-req4,
                    "general":x.populationnumber,
                    "under_1":x.childrennumber,
                    "calculate_for":cc_for

                }
                save_arr.append(save_data4)
                save_data5={
                    "facility":x.id,
                    "parent_fac":parent_save,
                    "level":x.level.id,
                    "code":x.code,
                    "condition":5,
                    "req_capacity":req5,
                    "available":capacity5,
                    "func_cap":fcapacity5,
                    "exces":fcapacity5-req5,
                    "calculate_for":cc_for,
                     "general":x.populationnumber,
                    "under_1":x.childrennumber,

                }
                save_arr.append(save_data5)
                for saves in save_arr:
                    save_ser=gapSaveSerializer(data=saves)
                    if save_ser.is_valid():
                        save_ser.save()
                    else:
                        print(save_ser.errors)
                ans.append(data)
            excel_data=[]
            for m in ans:
                new_data={
                    "Facility id":m["id"],
                    "Facility name":m["name"],
                    "Facility code":m["code"] ,
                    "Level name":m["level"],
                    "parent Facility ":m["parent"],
                    "general population":m["general"],
                    "under 1 population":m["children"],
                    "Facility type":m["type"]

                }    
                if(degree=="1"):
                    new_data["Total capacity for +2 to +8"]=m["tcapacity1"]
                    new_data["Functioning capacity for +2 to +8"]=m["fcapacity1"]
                    new_data["Required capacity for +2 to +8"]=m["req1"]
                    new_data["Diffrence between required capacity and available +2 to +8"]=m["excees1"]
                    if(data["exceed1"]):
                        new_data["Excess +2 to +8"]="True"
                    else:
                        new_data["Excess +2 to +8"]="False"    
                if(degree=="2"):
                    new_data["Total capacity for + -20C "]=m["tcapacity1"]
                    new_data["Functioning capacity for + -20C "]=m["fcapacity1"]
                    new_data["Required capacity for + -20C "]=m["req1"]
                    new_data["Diffrence between required capacity and available + -20C"]=m["excees1"]
                    if(data["exceed1"]):
                        new_data["Excess -20C"]="True"
                    else:
                        new_data["Excess -20C"]="False"   
                if(degree=="3"):
                    new_data["Total capacity for -70 C"]=m["tcapacity1"]
                    new_data["Functioning capacity for -70 C"]=m["fcapacity1"]
                    new_data["Required capacity for -70 C"]=m["req1"]
                    new_data["Diffrence between required capacity and available -70 C"]=m["excees1"]
                    if(data["exceed1"]):
                        new_data["Excess -70C"]="True"
                    else:
                        new_data["Excess -70C"]="False"   
                if(degree=="4"):
                    new_data["Total capacity for +25C"]=m["tcapacity1"]
                    new_data["Functioning capacity for +25C"]=m["fcapacity1"]
                    new_data["Required capacity for +25C"]=m["req1"]
                    new_data["Diffrence between required capacity and available +25C"]=m["excees1"]
                    if(data["exceed1"]):
                        new_data["Excess +25C"]="True"
                    else:
                        new_data["Excess +25C"]="False"   
                if(degree=="5"):
                    new_data["Total capacity for Dry store"]=m["tcapacity1"]
                    new_data["Functioning capacity for Dry store"]=m["fcapacity1"]
                    new_data["Required capacity for Dry store"]=m["req1"]
                    new_data["Diffrence between required capacity and available Dry store"]=m["excees1"]
                    if(data["exceed1"]):
                        new_data["Excess Dry store"]="True"
                    else:
                        new_data["Excess Dry store"]="False"   
                if(degree=="6"):
                    new_data["Total capacity for +2 to +8"]=m["tcapacity1"]
                    new_data["Functioning capacity for +2 to +8"]=m["fcapacity1"]
                    new_data["Required capacity for +2 to +8"]=m["req1"]
                    new_data["Diffrence between required capacity and available +2 to +8"]=m["excees1"]
                    if(data["exceed1"]):
                        new_data["Excess +2 to +8"]="True"
                    else:
                        new_data["Excess +2 to +8"]="False"
                    new_data["Total capacity for + -20C "]=m["tcapacity2"]
                    new_data["Functioning capacity for + -20C "]=m["fcapacity2"]
                    new_data["Required capacity for + -20C "]=m["req2"]
                    new_data["Diffrence between required capacity and available + -20C"]=m["excees2"]
                    if(data["exceed2"]):
                        new_data["Excess -20C"]="True"
                    else:
                        new_data["Excess -20C"]="False"
                    new_data["Total capacity for -70 C"]=m["tcapacity3"]
                    new_data["Functioning capacity for -70 C"]=m["fcapacity3"]
                    new_data["Required capacity for -70 C"]=m["req3"]
                    new_data["Diffrence between required capacity and available -70 C"]=m["excees3"]
                    if(data["exceed3"]):
                        new_data["Excess -70C"]="True"
                    else:
                        new_data["Excess -70C"]="False"    
                    new_data["Total capacity for +25C"]=m["tcapacity4"]
                    new_data["Functioning capacity for +25C"]=m["fcapacity4"]
                    new_data["Required capacity for +25C"]=m["req4"]
                    new_data["Diffrence between required capacity and available +25C"]=m["excees4"]
                    if(data["exceed4"]):
                        new_data["Excess +25C"]="True"
                    else:
                        new_data["Excess +25C"]="False"
                    new_data["Total capacity for Dry store"]=m["tcapacity5"]
                    new_data["Functioning capacity for Dry store"]=m["fcapacity5"]
                    new_data["Required capacity for Dry store"]=m["req5"]
                    new_data["Diffrence between required capacity and available Dry store"]=m["excees5"]
                    if(data["exceed5"]):
                        new_data["Excess Dry store"]="True"
                    else:
                        new_data["Excess Dry store"]="False"
                excel_data.append(new_data)
                

            deegre_str=""
            if(degree=="1"):
                deegre_str="2-8C"
            if(degree=="2"):
                deegre_str="-20C"
            if(degree=="3"):
                deegre_str="-70C"
            if(degree=="4"):
                deegre_str="+25C"
            if(degree=="5"):
                deegre_str="DryC"
            if(degree=="6"):
                deegre_str="all_conditions"
            print(deegre_str)    
            file_str=CountryConfig.objects.all().first().codecountry+"_"+str(deegre_str)+"_"+str(datetime.datetime.now()).split(".")[0].strip()+".xlsx"
            file_path = './media/gap_report.xlsx'
        
            if os.path.isfile(file_path):
                    os.remove(file_path)    
            df = pd.DataFrame(excel_data)
            df.to_excel('./media/'+file_str, index=False)  
            final_ans={
                "excel":'/media/'+file_str ,
                "data":ans
            }
            return Response(final_ans)

                    

class gapMapReport(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self,request):
        degree=request.query_params.get('degree')
        statuss=request.query_params.get('status')
        if(degree is None or  statuss is None ):
            return Response(status=status.HTTP_400_BAD_REQUEST)
        condition=int(degree)
        saved=gapSave.objects.filter(condition=condition)
        facilities_id=[]
        
        for z in saved:
            if(statuss=="2"):
                if(z.req_capacity-z.func_cap>0):
                    facilities_id.append(z.facility.id)
            if(statuss=="3"):
                if(z.req_capacity-z.func_cap<0):
                    facilities_id.append(z.facility.id)
            else:
                if(z.req_capacity-z.func_cap==0):
                    facilities_id.append(z.facility.id)
        all_fac=Facility.objects.filter(parentid=request.user.facilityid.id,is_deleted=False)
        all_fac=Facility.objects.filter(id=request.user.facilityid.id)|all_fac           
        
        ans=[]
        all_fac=all_fac.filter(id__in=facilities_id)
        for x in all_fac:
            if(x.gpsCordinate is not None):
                lat=float(x.gpsCordinate.split(",")[0].split("(")[1])
                lang=float(x.gpsCordinate.split(",")[1].split(")")[0])
                data={
                    "cordinates": [lat,lang]
                }
                ans.append(data)
        return Response(ans,status=status.HTTP_200_OK)


                                
class planGapView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self,request):
        help=request.query_params.get('help')
        if(help is None):
            return Response(status=status.HTTP_400_BAD_REQUEST)

        if(help=="true"):
            user=request.user
            this_facility=Facility.objects.filter(id=user.facilityid.id)[0]
            level=this_facility.level
            allow_levels=LevelConfig.objects.filter(id__gte=level.id)
            counter=CountryConfig.objects.all()[0]
            allow_levels=allow_levels.filter(id__lte=counter.levels)
            levels=levelSerializer(allow_levels,many=True)
            power=facilityParamDescription.objects.filter(paramid=10,enabled=True)
            powerss=facilityParamDescriptionSerilizer(power,many=True)
            type=facilityParamDescription.objects.filter(paramid=12,enabled=True)
            typess=facilityParamDescriptionSerilizer(type,many=True)
            l_data=[]

            for x in levels.data:
                data={
                    "name":x["name"],
                    "id":x["id"]
                }
                l_data.append(data)
            datas={
                "level":l_data,
                "type":typess.data,
                "power":powerss.data,
            }
            return Response(datas,status=status.HTTP_200_OK)
        else:
            name=request.query_params.get('name',None)
            level=request.query_params.get('level',None)
            type=request.query_params.get('type',None)
            power=request.query_params.get('power',None)
            code=request.query_params.get('code',None)
            degree=request.query_params.get('degree',None)
            general_from=request.query_params.get('general_from',None)
            general_to=request.query_params.get('general_to',None)
            under_1_from=request.query_params.get('under_1_from',None)
            under_1_to=request.query_params.get('under_1_to',None)
            req_cap_to=request.query_params.get('req_cap_to',None)
            req_cap_from=request.query_params.get('req_cap_from',None)
            available_from=request.query_params.get('available_from',None)
            available_to=request.query_params.get('available_to',None)
            func_cap_from=request.query_params.get('func_cap_from',None)
            func_cap_to=request.query_params.get('func_cap_to',None)
            excees_from=request.query_params.get('excees_from',None)
            excees_to=request.query_params.get('excees_to',None)
            facility=Facility.objects.filter(parentid=request.user.facilityid.id,is_deleted=False)
            facility=Facility.objects.filter(id=request.user.facilityid.id)|facility
            if(name is not None):
                facility=facility.filter(name__icontains=name)
            if(level is not None):
                facility=facility.filter(level=level)
            if(type is not None):
                facility=facility.filter(type=type)
            if(power is not None):
                facility=facility.filter(powersource=power)
            if(code is not None):
                facility=facility.filter(code__icontains=code)
            gap_save=gapSave.objects.filter(facility__in=facility)
            if(degree is not None):
                degree=int(degree)
                gap_save=gap_save.filter(condition=degree)
            if(general_from is not None):
                gap_save=gap_save.filter(general__gte=general_from)
            if(general_to is not None):
                gap_save=gap_save.filter(general__lte=general_to)
            if(under_1_from is not None):
                gap_save=gap_save.filter(under_1__gte=under_1_from)
            if(under_1_to is not None):
                gap_save=gap_save.filter(under_1__lte=under_1_to)
            if(req_cap_from is not None):
                gap_save=gap_save.filter(req_capacity__gte=req_cap_from)
            if(req_cap_to is not None):
                gap_save=gap_save.filter(req_capacity__lte=req_cap_to)
            if(available_from is not None):
                gap_save=gap_save.filter(available__gte=available_from)
            if(available_to is not None):
                gap_save=gap_save.filter(available__lte=available_to)
            if(func_cap_from is not None):
                gap_save=gap_save.filter(func_cap__gte=func_cap_from)
            if(func_cap_to is not None):
                gap_save=gap_save.filter(func_cap__lte=func_cap_to)
            if(excees_from is not None):
                gap_save=gap_save.filter(exces__gte=excees_from)
            if(excees_to is not None):
                gap_save=gap_save.filter(exces__lte=excees_to)
            ans=[]
            for x in gap_save:
                type_name=""
                if(x.facility.type is not None):
                    type_name=get_object_or_404(facilityParamDescription,id=x.facility.type).name
                power_name=""
                if(x.facility.powersource != None):
                    power_name=get_object_or_404(facilityParamDescription,id=x.facility.powersource).name

                    
                parent="--"
                if(x.parent_fac is not None):
                    parent=x.parent_fac.name
                condition="--"
                if(x.condition ==1):
                    condition="2-8 C"
                if(x.condition ==2):
                    condition="-20 C"
                if(x.condition ==3):
                    condition="-70 C"
                if(x.condition ==4):
                    condition="+25 C"
                if(x.condition ==5):
                    condition="Dry store"                    
                data={
                     "id":x.id,
                    "facility":x.facility.name,
                    "parent":parent,
                    "level":x.level.id,
                    "code":x.code,
                    "type":type_name,
                    "power":power_name,
                    "req_capacity":x.req_capacity,
                    "available":x.available,
                    "func_cap":x.func_cap,
                    "exces":x.exces,
                    "condition":condition,
                    "planned":x.planned,
                    
                   
                }
                ans.append(data)
            return Response(ans,status=status.HTTP_200_OK)    


class planOneGapView(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self,request):
        data=request.data
        gap=gapSave.objects.get(id=data["id"])
        gap.planned=True
        gap.save()
        count=data["count"]
        new_data={
            "gap":gap.id,
                "pqs_type":data["type"],
                "pqs_id":data["pqs_id"],
        }
        ans=[]
        code=""
        vac_cap=0
        freez_cap=0
        type=""
        if(data["type"]==3):
                finded=get_object_or_404(pqs3,id=data["pqs_id"])
                code=finded.pqscode
                vac_cap=finded.refrigeratorcapacity
                freez_cap=finded.freezercapacity
                type=finded.description

                
        else:
                finded=get_object_or_404(pqs4,id=data["pqs_id"])
                code=finded.pqsnumber
                vac_cap=finded.vaccinenetstoragecapacity
                freez_cap=finded.coolantpacknominalcapacity
                type=finded.type
        for i in range(int(count)):
            ser=plannedSerializer(data=new_data)
            if(ser.is_valid()):
                ser.save()
                

            else:
                print(ser.errors)
        palns=plannedGap.objects.filter(gap=gap.id)
        table=[]
        for x in palns:
            code=""
            vac_cap=0
            freez_cap=0
            type=""
            if(x.pqs_type==3):
                    finded=get_object_or_404(pqs3,id=x.pqs_id)
                    code=finded.pqscode
                    vac_cap=finded.refrigeratorcapacity
                    freez_cap=finded.freezercapacity
                    type=finded.description

                    
            else:
                    finded=get_object_or_404(pqs4,id=x.pqs_id)
                    code=finded.pqsnumber
                    vac_cap=finded.vaccinenetstoragecapacity
                    freez_cap=finded.coolantpacknominalcapacity
                    type=finded.type
            data={
                "id":x.id,
                "facility":x.gap.facility.name,
                "code":code,
                "type":type,
                "vac_cap":vac_cap,
                "freez_cap":freez_cap,
                "assigned":x.asiign,
            }
            table.append(data)
        return Response(table,status=status.HTTP_200_OK)

    def get(self,request):
        id=request.query_params.get('id',None)
        pqs=request.query_params.get('pqs_id',None)
        type=request.query_params.get('type',None)
        if(id is None):
            return Response(status=status.HTTP_400_BAD_REQUEST)
        if(pqs is None):
            palns=plannedGap.objects.filter(gap=id)
            table=[]
            for x in palns:
                code=""
                vac_cap=0
                freez_cap=0
                type=""
                if(x.pqs_type==3):
                        finded=get_object_or_404(pqs3,id=x.pqs_id)
                        code=finded.pqscode
                        vac_cap=finded.refrigeratorcapacity
                        freez_cap=finded.freezercapacity
                        type=finded.description

                        
                else:
                        finded=get_object_or_404(pqs4,id=x.pqs_id)
                        code=finded.pqsnumber
                        vac_cap=finded.vaccinenetstoragecapacity
                        freez_cap=finded.coolantpacknominalcapacity
                        type=finded.type
                data={
                    "id":x.id,
                    "facility":x.gap.facility.name,
                    "code":code,
                    "type":type,
                    "vac_cap":vac_cap,
                    "freez_cap":freez_cap,
                    "assigned":x.asiign,
                }
                table.append(data)
            y=get_object_or_404(gapSave,id=id)
            type_name=""
            if(y.facility.type is not None):
                type_name=get_object_or_404(facilityParamDescription,id=y.facility.type).name
            power_name=""
            if(y.facility.powersource != None):
                power_name=get_object_or_404(facilityParamDescription,id=y.facility.powersource).name

                
            parent="--"
            if(y.parent_fac is not None):
                parent=y.parent_fac.name
            condition="--"
            if(y.condition ==1):
                condition="2-8 C"
            if(y.condition ==2):
                condition="-20 C"
            if(y.condition ==3):
                condition="-70 C"
            if(y.condition ==4):
                condition="+25 C"
            if(y.condition ==5):
                condition="Dry store"                    
            gap_Ser={
                "id":y.id,
                "facility":y.facility.name,
                "parent":parent,
                "level":y.level.id,
                "code":y.code,
                "type":type_name,
                "power":power_name,
                "req_capacity":y.req_capacity,
                "available":y.available,
                "func_cap":y.func_cap,
                "exces":y.exces,
                "condition":condition,
                "planned":y.planned,
                
            }
            pqs3_data=pqs3.objects.all()
            ans=[]
            for x in pqs3_data:
                data={
                    "id":x.id,
                    "name":x.description+x.refrigeratorcapacity,
                    "pqs":3
                }
                ans.append(data)
            pqs4_ser=pqs4.objects.all()   
            for z in pqs4_ser:
                data={
                    "id":z.id,
                    "name":z.pqsnumber+z.vaccinenetstoragecapacity,
                    "pqs":4
                }
                ans.append(data)
            final_ans={
                "data":gap_Ser,
                "pqs":ans,
                "table":table
            }
            return Response(final_ans,status=status.HTTP_200_OK)
        else:
            palns=plannedGap.objects.filter(gap=id)
            table=[]
            for x in palns:
                code=""
                vac_cap=0
                freez_cap=0
                type=""
                if(x.pqs_type==3):
                        finded=get_object_or_404(pqs3,id=x.pqs_id)
                        code=finded.pqscode
                        vac_cap=finded.refrigeratorcapacity
                        freez_cap=finded.freezercapacity
                        type=finded.description

                        
                else:
                        finded=get_object_or_404(pqs4,id=x.pqs_id)
                        code=finded.pqsnumber
                        vac_cap=finded.vaccinenetstoragecapacity
                        freez_cap=finded.coolantpacknominalcapacity
                        type=finded.type
                data={
                    "id":x.id,
                    "facility":x.gap.facility.name,
                    "code":code,
                    "type":type,
                    "vac_cap":vac_cap,
                    "freez_cap":freez_cap,
                    "assigned":x.asiign,
                }
                table.append(data)
            finded=None
            ser=None
            if(type=="3"):
                finded=get_object_or_404(pqs3,id=pqs)
                ser=pqs3Serializer(finded,many=False)
            else:
                finded=get_object_or_404(pqs4,id=pqs)
                ser=pqs4Serializer(finded,many=False)
            final_ans={
                "data":ser.data,
                "table":table
            }    
            return Response(final_ans,status.HTTP_200_OK)    

    def put(self,request):
        plan=get_object_or_404(plannedGap,id=request.data["id"])
        gap_save=get_object_or_404(gapSave,id=plan.gap.id)
        gap_save.planned=True
        gap_save.save()
        plan.provided=True
        plan.asiign=True
        plan.save()
        return Response({"message":"success"},status=status.HTTP_200_OK)
    def delete(self,request):
        plan=get_object_or_404(plannedGap,id=request.data["id"])
        plan.delete()
        return Response({"message":"success"},status=status.HTTP_200_OK)

                
class plannedSavedReport(APIView):
    permission_classes=(IsAuthenticated,)
    def get(self,request):
        help=request.query_params.get('help')
        if(help is None):
            return Response(status=status.HTTP_400_BAD_REQUEST)

        if(help=="true"):
            user=request.user
            this_facility=Facility.objects.filter(id=user.facilityid.id)[0]
            level=this_facility.level
            allow_levels=LevelConfig.objects.filter(id__gte=level.id)
            counter=CountryConfig.objects.all()[0]
            allow_levels=allow_levels.filter(id__lte=counter.levels)
            levels=levelSerializer(allow_levels,many=True)
            power=facilityParamDescription.objects.filter(paramid=10,enabled=True)
            powerss=facilityParamDescriptionSerilizer(power,many=True)
            type=facilityParamDescription.objects.filter(paramid=12,enabled=True)
            typess=facilityParamDescriptionSerilizer(type,many=True)
            l_data=[]

            for x in levels.data:
                data={
                    "name":x["name"],
                    "id":x["id"]
                }
                l_data.append(data)
            datas={
                "level":l_data,
                "type":typess.data,
                "power":powerss.data,
            }
            return Response(datas,status=status.HTTP_200_OK)
        else:
            name=request.query_params.get('name',None)
            level=request.query_params.get('level',None)
            type=request.query_params.get('type',None)
            power=request.query_params.get('power',None)
            code=request.query_params.get('code',None)
            degree=request.query_params.get('degree',None)
            general_from=request.query_params.get('general_from',None)
            general_to=request.query_params.get('general_to',None)
            under_1_from=request.query_params.get('under_1_from',None)
            under_1_to=request.query_params.get('under_1_to',None)
            req_cap_to=request.query_params.get('req_cap_to',None)
            req_cap_from=request.query_params.get('req_cap_from',None)
            available_from=request.query_params.get('available_from',None)
            available_to=request.query_params.get('available_to',None)
            func_cap_from=request.query_params.get('func_cap_from',None)
            func_cap_to=request.query_params.get('func_cap_to',None)
            excees_from=request.query_params.get('excees_from',None)
            excees_to=request.query_params.get('excees_to',None)
            facility=Facility.objects.all()
            if(name is not None):
                facility=facility.filter(name__icontains=name)
            if(level is not None):
                facility=facility.filter(level=level)
            if(type is not None):
                facility=facility.filter(type=type)
            if(power is not None):
                facility=facility.filter(powersource=power)
            if(code is not None):
                facility=facility.filter(code__icontains=code)
            gap_save=gapSave.objects.filter(facility__in=facility)
            if(degree is not None):
                degree=int(degree)
                gap_save=gap_save.filter(condition=degree)
            if(general_from is not None):
                gap_save=gap_save.filter(general__gte=general_from)
            if(general_to is not None):
                gap_save=gap_save.filter(general__lte=general_to)
            if(under_1_from is not None):
                gap_save=gap_save.filter(under_1__gte=under_1_from)
            if(under_1_to is not None):
                gap_save=gap_save.filter(under_1__lte=under_1_to)
            if(req_cap_from is not None):
                gap_save=gap_save.filter(req_capacity__gte=req_cap_from)
            if(req_cap_to is not None):
                gap_save=gap_save.filter(req_capacity__lte=req_cap_to)
            if(available_from is not None):
                gap_save=gap_save.filter(available__gte=available_from)
            if(available_to is not None):
                gap_save=gap_save.filter(available__lte=available_to)
            if(func_cap_from is not None):
                gap_save=gap_save.filter(func_cap__gte=func_cap_from)
            if(func_cap_to is not None):
                gap_save=gap_save.filter(func_cap__lte=func_cap_to)
            if(excees_from is not None):
                gap_save=gap_save.filter(exces__gte=excees_from)
            if(excees_to is not None):
                gap_save=gap_save.filter(exces__lte=excees_to)
            plans=plannedGap.objects.filter(gap__in=gap_save)
            table=[]
            for x in plans:
                code=""
                vac_cap=0
                freez_cap=0
                type=""
                if(x.pqs_type==3):
                        finded=get_object_or_404(pqs3,id=x.pqs_id)
                        code=finded.pqscode
                        vac_cap=finded.refrigeratorcapacity
                        freez_cap=finded.freezercapacity
                        type=finded.description

                        
                else:
                        finded=get_object_or_404(pqs4,id=x.pqs_id)
                        code=finded.pqsnumber
                        vac_cap=finded.vaccinenetstoragecapacity
                        freez_cap=finded.coolantpacknominalcapacity
                        type=finded.type
                data={
                    "id":x.id,
                    "facility":x.gap.facility.name,
                    "code":code,
                    "type":type,
                    "vac_cap":vac_cap,
                    "freez_cap":freez_cap,
                    "assigned":x.asiign,
                }
                table.append(data)
            return Response(table,status=status.HTTP_200_OK)    




        






                


                


            
        
