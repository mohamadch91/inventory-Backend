from typing import final
from xmlrpc.client import APPLICATION_ERROR
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from re import I
from django.shortcuts import render

# Create your views here.
import json
from os import stat
from urllib import request, response
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
from facilities.models import *
from facilities.serializers import *
from items.models import *
from items.serializers import *
from PQS.models import *
from PQS.serializers import *
import copy
from maintanance.models import *
from maintanance.serializers import *
import datetime
import pandas
class itemView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        
        new_data=copy.deepcopy(request.data)
        x=int(new_data["same_item"])
        ans=[]
        for i in range(x):
            facility=new_data["facility"]
            facility=get_object_or_404(Facility, id=facility)
            item_class=new_data["item_class"]
            item_type=new_data["item_type"]
            item_class=get_object_or_404(ItemClass, id=item_class)
            item_type=get_object_or_404(ItemType, id=item_type)   
            if(item.objects.filter(facility=facility,item_class=item_class.id,item_type=item_type.id).count()==0):
                item_code=f"{1:03d}"    
            else:
                item_count=item.objects.filter(facility=facility,item_class=item_class.id,item_type=item_type.id).count()
                item_code=f"{item_count+1:03d}"    
            new_data["code"]=f"{facility.code}{item_class.code}{item_type.code}{item_code}"
            serializer = itemSerializer(data=new_data)
            if serializer.is_valid():
                serializer.save()
                ans.append(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(ans,status=status.HTTP_201_CREATED)
    def get(self, request):
        id=request.query_params.get('id',None)
        facility=request.query_params.get('facility',None)
        deleted=request.query_params.get('isDel',False)
        item_class=request.query_params.get('item_class',None)
        item_type=request.query_params.get('item_type',None)
        code=request.query_params.get('code',None)
        physical=request.query_params.get('physical',None)
        working=request.query_params.get('working',None)
        year_from=request.query_params.get('yfrom',None)
        year_to=request.query_params.get('yto',None)
        func=request.query_params.get('functioning',None)
        items=item.objects.all()
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
            items=items.filter(code__icontains=code)
        if(func is not None):
            if(func=="true"):
                items=items.filter(IsItFunctioning=True)
            else:
                items=items.filter(IsItFunctioning=False)
        if(deleted=="true"):
            items=items.filter(isDel=True)
        else:
            items=items.filter(isDel=False)
        
        if(facility is not None):
            country=items.filter(facility=facility,isDel=False)
            serializer =  itemSerializer(country, many=True)
            new_data=copy.deepcopy(serializer.data)
            for i in new_data:
                if(i["Manufacturer"] is not None):
                    man=get_object_or_404(Manufacturer,id=i["Manufacturer"])
                    i["Manufacturer"]=man.describe
            sored_data=sorted(new_data, key=lambda k: k['id'])
            return Response(sored_data)
        if(id is not None):    
            country = item.objects.filter(id=id,isDel=False)
            serializer =  itemSerializer(country, many=True)
            new_data=copy.deepcopy(serializer.data)
            sored_data=sorted(new_data, key=lambda k: k['id'])
            return Response(sored_data)
            
        items=items.filter(facility=request.user.facilityid,isDel=False)       
        serializer =  itemSerializer(items, many=True)
        new_data=copy.deepcopy(serializer.data)
        for i in new_data:
            if(i["Manufacturer"] is not None):
                man=get_object_or_404(Manufacturer,id=i["Manufacturer"])
                i["Manufacturer"]=man.describe
        sored_data=sorted(new_data, key=lambda k: k['id'])
        return Response(sored_data)

    def put(self, request, ):
        id=request.data["id"]
        country = get_object_or_404(item, id=id)
        serializer =  itemSerializer(country, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        id=request.data["id"]
        facility = get_object_or_404(item, id=id)
        facility.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class itemFieldView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        user=request.user
        class_id=request.query_params.get('class_id', None)
        type_id=request.query_params.get('type_id', None)
        parent=request.query_params.get('parent',None)
        
        if class_id is None and type_id is None:
            facility=user.facilityid
            facility=get_object_or_404(Facility, id=facility.id)
            if(parent is not None and parent!=""):
                facility=get_object_or_404(Facility,id=parent)
                
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
                    new_data={
                        "id":k.id,
                        "title":k.code+" - "+k.title,
                        "havepqs":k.havePQS,
                    }
                    second_data.append(new_data)
                data={
                    "item_class":{
                        "id":x.id,
                        "title":x.code +" - " +x.title,

                    },
                    "item_type":second_data,
                }
                first_data.append(data)
            fac_data={
            "id":fac_ser.data["id"],
            "name":fac_ser.data["name"]+" - " +fac_ser.data["code"][3:],
            "code":fac_ser.data["code"],
            "level":fac_ser.data["level"],
        }    
            ans={
                "facility":fac_data,
                "data":first_data
            }    
            return Response(ans)
        else:
            facility=user.facilityid
            facility=get_object_or_404(Facility, id=facility.id)
            if(parent is not None):
                facility=get_object_or_404(Facility,id=parent)
            fac_ser=facilitySerializer(facility,many=False)
            fac_data={
            "id":fac_ser.data["id"],
            "name":fac_ser.data["name"]+" - " +fac_ser.data["code"][3:],
            "code":fac_ser.data["code"],
            "level":fac_ser.data["level"],
        }    
            item_class=get_object_or_404(ItemClass,id=class_id)
            item_type=get_object_or_404(ItemType,id=type_id)
            ans={}
            Manufacturers=Manufacturer.objects.filter(active=True,itemclass=item_class.id)
            man_Ser=ManufacturerSerializer(Manufacturers,many=True)    
            related=relatedItemType.objects.filter(itemtype=item_type.id)
            related=related.order_by('id')
            fields=[]
            same_item={}
            same_item['field']={
                "id":877,
                "name":"Number of the same items with the same condition in this facility",
                "params":[],
                "required":False,
                "state":"same_item",
                "topic":"Other additional and optional fields",
                "type":"number",
                "validation":[
                    {
                        "id":877,
                        "digits":4,
                        "min":1,
                        "max":1000,
                        "float":False,
                        "floating":-1,
                        "fieldid":877,
                    }
                ],
            }
            fields.append(same_item)
            for x in related:
                data={}
                field=Field.objects.get(id=x.field.id)
                field_ser=fieldSerializer(field,many=False)
                copys=copy.deepcopy(field_ser.data)
                data["field"]=copys
                data["field"]["required"]=x.required
                if(field.id==2):
                   
                    data["field"]["params"]=man_Ser.data
                else:
                    try:
                        param=itemParam.objects.get(fieldid=field.id)
            #    if(param.count()>0):
                        params=itemParamSerilizer(param,many=False)                        
                        describe=itemParamDescription.objects.filter(paramid=params.data["id"],enabled=True)
                        des_ser=itemParamDescriptionSerilizer(describe,many=True) 
                        data["field"]["params"]=des_ser.data
            #    else:
                    except:
                        data["field"]["params"]=[]    
                    if(field.id==76):
                        maint=maintancegp.objects.filter(enable=True,item_class=item_class.id,item_type=item_type.id)
                        maint_ser=maintancegpSerializers(maint,many=True)
                        data["field"]["params"]=maint_ser.data 
                    if(field.id==31):
                        data1= {
                    "id": 1,
                    "describe": "+25C",
                    "active": True,
                    "order": 1,
                    "itemclass": 1
                }
                        data2= {
                    "id": 2,
                    "describe": "+2 - +8 C",
                    "active": True,
                    "order": 1,
                    "itemclass": 1
                }
                        data3= {
                    "id": 3,
                    "describe": "-20 C",
                    "active": True,
                    "order": 1,
                    "itemclass": 1
                }
                        data4={
                    "id": 4,
                    "describe": "-70 C",
                    "active": True,
                    "order": 1,
                    "itemclass": 1
                }
                        data5={
                    "id": 5,
                    "describe": "Dry store",
                    "active": True,
                    "order": 1,
                    "itemclass": 1
                }
                        ic_id=item_class.id
                        it_id=item_type.id
                        ans=[]
                        if(ic_id==1):
                            if(it_id==1 or it_id==3 or it_id==5):
                                ans.append(data2)
                            elif(it_id==2 or it_id==4):
                                ans.append(data3)
                            elif(it_id==6):
                                ans.append(data4)
                            else:
                                ans.append(data1)
                                ans.append(data2)
                                ans.append(data3)
                                ans.append(data4)
                                ans.append(data5)
                        else:
                            ans.append(data1)
                            ans.append(data2)
                            ans.append(data3)
                            ans.append(data4)
                            ans.append(data5)                    
                 
                 
                 
                 
                        data["field"]["params"]=ans


                         
                val=Itemvalidation.objects.filter(fieldid=x.field.id)
                val_ser=ItemvalidationSerilizer(val,many=True)

                if(val.count()>0):
                    data["field"]["validation"]=val_ser.data
                else:
                    data["field"]["validation"]=[]  
                fields.append(data)
            #sort field by order
            fields=sorted(fields, key=lambda k: k['field']['id'])
            final={
                "facility":fac_data,
                "fields":fields
            }    
          
            return Response(final)       



class itemPQSView(APIView):

    def get(self,request):
        id=request.query_params.get('id',None)
        if(id is not None):

            item_type=get_object_or_404(ItemType,id=id)
            item_class=get_object_or_404(ItemClass,id=item_type.itemclass.id)

            if(item_class.code=='ACC'):
                tcode=item_type.code
                if(tcode=='REF' or tcode=='FRZ' or tcode=='CRF' or tcode=='UFR' or tcode=='IFR' ):
                    pqs=pqs3.objects.all()
                    ser=pqs3Serializer(pqs,many=True)
                    new_Data=copy.deepcopy(ser.data)
                    for i in new_Data:
                        i["ptype"]=3
                    return Response(new_Data,status=status.HTTP_200_OK)
                else:
                    pqss=pqs3.objects.all()
                    ser=pqs3Serializer(pqss,many=True)
                    new_Data=copy.deepcopy(ser.data)
                    for i in new_Data:
                        i["ptype"]=3
                    pqs44=pqs4.objects.all()
                    ser4=pqs4Serializer(pqs44,many=True)
                    new_Data4=copy.deepcopy(ser4.data)
                    for i in new_Data4:
                        i["ptype"]=4
                    ans=new_Data+new_Data4
                    return Response(ans,status=status.HTTP_200_OK)       

            if(item_class.code=='PCC'):
                tcode=item_type.code
                if(tcode=='CBX' or tcode=='VCX'):
                    pqs44=pqs4.objects.all()
                    ser4=pqs4Serializer(pqs44,many=True)
                    new_Data4=copy.deepcopy(ser4.data)
                    for i in new_Data4:
                        i["ptype"]=4
                    return Response(new_Data4,status=status.HTTP_200_OK)
                else:
                    pqss=pqs3.objects.all()
                    ser=pqs3Serializer(pqss,many=True)
                    new_Data=copy.deepcopy(ser.data)
                    for i in new_Data:
                        i["ptype"]=3
                    pqs44=pqs4.objects.all()
                    ser4=pqs4Serializer(pqs44,many=True)
                    new_Data4=copy.deepcopy(ser4.data)
                    for i in new_Data4:
                        i["ptype"]=4
                    ans=new_Data+new_Data4
                    return Response(ans,status=status.HTTP_200_OK)        
            else:
                pqss=pqs3.objects.all()
                ser=pqs3Serializer(pqss,many=True)
                new_Data=copy.deepcopy(ser.data)
                for i in new_Data:
                    i["ptype"]=3
                pqs44=pqs4.objects.all()
                ser4=pqs4Serializer(pqs44,many=True)
                new_Data4=copy.deepcopy(ser4.data)
                for i in new_Data4:
                    i["ptype"]=4
                ans=new_Data+new_Data4
                return Response(ans,status=status.HTTP_200_OK)     
        else:
                
                return Response([],status=status.HTTP_200_OK)   

            
class itemdb(APIView):
    def get(self,request):
        excel_data_df = pandas.read_excel('titem.xlsx', sheet_name='Items')
        excel_data_df.fillna("###", inplace=True)
        counter=0
        for i in range(len(excel_data_df)): 
            z=int(excel_data_df['isDel'][i])
            if(z==0):
                counter+=1
                dic={
                "OtherCode":excel_data_df['code'][i],
                "facility":excel_data_df['facilitycode'][i],
                "item_type":excel_data_df['itemtype'][i],
                "item_class":excel_data_df['itemclass'][i],
                "WorkingConditions":excel_data_df['workingCondition'][i],
                "StorageConditions":excel_data_df['temprange'][i],
                "EnergySource_generator":excel_data_df['energysource'][i],
                "Manufacturer":excel_data_df['Manufacturer'][i],
                "TypeP":excel_data_df['type'][i],
                "Type2":excel_data_df['type2'][i],
                "Type3":excel_data_df['type3'][i],
                "Model":excel_data_df['model'][i],
                "NetVaccineStorageCapacity":excel_data_df['netVaccCapacity'][i],
                "FreezerNetCapacity":excel_data_df['capacity'][i],
                "IceMakingCapacity":excel_data_df['iceCapacity'][i],
                "CoolWaterProductionCapacity":excel_data_df['coolWaterCapacity'][i],
                "RefrigerantGas":excel_data_df['refrigrationgas'][i],
                "IsTheRefrigerantGasCFCFree":excel_data_df['CFCFree'][i],
                "PQSPISManufacturer":excel_data_df['pqsmanufacturer'][i],
                "PQSPISRefrigerantGas":excel_data_df['pqsrefgas'][i],
                "PQSPISTemperatureWorkingZone":excel_data_df['pqstempzone'][i],
                "PQSPISCode":excel_data_df['PQSCode'][i],
                "PQSPISType":excel_data_df['pqstype'][i],
                "Height":excel_data_df['height'][i],
                "Width":excel_data_df['width'][i],
                "Length":excel_data_df['length'][i],
                "Weightkg":excel_data_df['Weight'][i],
                "GrossVolume":excel_data_df['grossVolume'][i],
                "NetShippingVolume":excel_data_df['netVolume'][i],
                "Weightkg":excel_data_df['Weight'][i],
                "DoesItHaveFreezingCompartment":True,
                "NumberOfCoolingUnits":excel_data_df['coolingUnitNumber'][i],
                "DoesItHaveContinuousTemperatureMonitoringDevice":True,
                "DoesItHaveAnAlarmSystem":excel_data_df['haveAlarm'][i],
                "DoesItHaveBuiltInThermometer":True,
                "DoesItHaveFreezingCompartment":True,
                "DoesItHaveAnExtraFuelTank":True,
                "WorkingTemperatureRange":excel_data_df['tempzone'][i],
                "Voltage":excel_data_df['voltage'][i],
                "Phase":excel_data_df['phase'][i],
                "IsItFunctioning":excel_data_df['inUse'][i],
                "NotInUseSince":excel_data_df['notUseDate'][i],
                "ReasonsForNotFunctioning":excel_data_df['notUseCouse'][i],
                "FinancialSource":excel_data_df['FinancialSource'][i],
                "DoesTheDryStoreHaveAdequateLighting":True,
                "DoesTheDryStoreHaveHeating":False,
                "DoesTheDryStoreHaveAirConditioning":False,
                "IsTheDryStorageAreaProtectedFromDirectSunlight":True,
                "DSHaveShelves":True,
                "IsTheDryStorageAreaClean":True,
                "OtherFieldsItem1":excel_data_df['description'][i],
                "YearInstalled":excel_data_df['installYear'][i],
                "IsThereAnAutomaticStartUpSystem":True,
                "EnergySource":excel_data_df['powerGeneration'][i],
                "PhysicalConditions":excel_data_df['physicalCondition'][i],
                "TechnicalConditions":excel_data_df['TechnicalCondition'][i],
                "OriginalCost":excel_data_df['originalCost'][i],
                "IsThereAnAutomaticStartUpSystem":excel_data_df['autoStart'][i],
                "CoolantPackNominalCapacity":excel_data_df['CoolantPackNominalCapacity'][i],
                "NumberOfCoolantPacksRequired":excel_data_df['coolantpacknumber'][i],
                }
                ## iterate all keys and check for  ### value

                dic_copy=dic.copy()
                for i in dic.keys():
                    if(dic[i] == "###"):
                        del dic_copy[i]
                dic=dic_copy
                # print(dic)
                facilty=Facility.objects.filter(other_code=dic['facility'].strip())
                if(facilty.count()==0):
                    print("not found")
                    continue
                facilty=facilty[0]
                dic['facility']=facilty.id
                item_class_code=dic['OtherCode'].strip()[10:13]
                # print(item_class_code)
                item_class=ItemClass.objects.filter(title__icontains=item_class_code)
                # if(item_class.count()==0):
                #     item_class=ItemClass.objects.filter(title__icontains='Active equipment')[0]
                # else:
                item_class=item_class[0]


                dic['item_class']=item_class.id
                item_type=ItemType.objects.filter(title__icontains=dic['item_type'].strip())
                if(item_type.count()==0):
                    obj={
                        "title":dic['item_type'].strip(),
                        "active":True,
                        "havePQS":False,
                        "itemclass":item_class.id
                    }

                    num=item_class.itemtype_set.count()
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
                        dic['item_type']=serializer.data['id']
                        item_type=ItemType.objects.filter(id=serializer.data['id'])[0]
                        
                else:   
                    item_type=item_type[0]
                    dic['item_type']=item_type.id
                if(item.objects.filter(facility=facilty,item_class=item_class.id,item_type=item_type.id).count()==0):
                    item_code=f"{1:03d}"    
                else:
                    item_count=item.objects.filter(facility=facilty,item_class=item_class.id,item_type=item_type.id).count()
                    item_code=f"{item_count+1:03d}"    
                dic["code"]=f"{facilty.code}{item_class.code}{item_type.code}{item_code}"

                if  'WorkingConditions' in dic   and ((dic['WorkingConditions']!=None) or dic['WorkingConditions']!=""):
                    new_ownership=itemParamDescription.objects.filter(name__icontains=dic['WorkingConditions'].strip())
                    if(new_ownership.count()>0):
                        dic['WorkingConditions']=new_ownership[0].id
                    else:
                        temp_param={
                            "name":dic['WorkingConditions'],
                            "paramid":11,
                            "enabled":True,
                            "order":1
                        }
                        ser=itemParamDescriptionSerilizer(data=temp_param)
                        if(ser.is_valid()):
                            ser.save()
                            dic['WorkingConditions']=ser.data["id"]
                
                if  'EnergySource' in dic   and ((dic['EnergySource']!=None) or dic['EnergySource']!=""):
                    if(dic['EnergySource']==-1):
                        dic['EnergySource']="EG"
                    elif dic['EnergySource']==154:
                        dic['EnergySource']="დიზელი"
                    elif dic['EnergySource']==155:
                        dic['EnergySource']="ბენზინი"
                    new_ownership=itemParamDescription.objects.filter(name__icontains=dic['EnergySource'].strip())
                    if(new_ownership.count()>0):
                        dic['EnergySource']=new_ownership[0].id
                    else:
                        temp_param={
                            "name":dic['EnergySource'],
                            "paramid":12,
                            "enabled":True,
                            "order":1
                        }
                        ser=itemParamDescriptionSerilizer(data=temp_param)
                        if(ser.is_valid()):
                            ser.save()
                            dic['EnergySource']=ser.data["id"]
                if 'StorageConditions' in dic   and ((dic['StorageConditions']!=None) or dic['StorageConditions']!=""):
                    sg=dic['StorageConditions']
                    if(sg=='2-8 C'):
                        dic['StorageConditions']="2"
                    elif(sg=='-20 C'):
                        dic['StorageConditions']="3"
                    elif(sg=='-80 C'):
                        dic['StorageConditions']="4"
                    elif(sg=='+25 C'):
                        dic['StorageConditions']="1"
                    else:
                        dic['StorageConditions']=""
                if 'Manufacturer' in dic   and ((dic['Manufacturer']!=None) or dic['Manufacturer']!=""):
                    Manufacturers=Manufacturer.objects.filter(describe__icontains=dic['Manufacturer'].strip())
                    if(Manufacturers.count()>0):
                        dic['Manufacturer']=Manufacturers[0].id
                    else:
                        temp_param={
                            "describe":dic['Manufacturer'].strip(),
                            "enabled":True,
                            "order":1,
                            "itemclass":item_class.id,
                        }
                        ser=ManufacturerSerializer(data=temp_param)
                        if(ser.is_valid()):
                            ser.save()
                            dic['Manufacturer']=ser.data["id"]
                if 'TypeP' in dic   and ((dic['TypeP']!=None) or dic['TypeP']!=""):
                    types=itemParamDescription.objects.filter(name__icontains=dic['TypeP'].strip())
                    if(types.count()>0):
                        dic['TypeP']=types[0].id
                    else:
                        temp_param={
                            "name":dic['TypeP'],
                            "paramid":1,
                            "enabled":True,
                            "order":1
                        }
                        ser=itemParamDescriptionSerilizer(data=temp_param)
                        if(ser.is_valid()):
                            ser.save()
                            dic['TypeP']=ser.data["id"]
                if 'Type2' in dic   and ((dic['Type2']!=None) or dic['Type2']!=""):
                    types=itemParamDescription.objects.filter(name__icontains=dic['Type2'].strip())
                    if(types.count()>0):
                        dic['Type2']=types[0].id
                    else:
                        temp_param={
                            "name":dic['Type2'],
                            "paramid":4,
                            "enabled":True,
                            "order":1
                        }
                        ser=itemParamDescriptionSerilizer(data=temp_param)
                        if(ser.is_valid()):
                            ser.save()
                            dic['Type2']=ser.data["id"]
                if 'Type3' in dic   and ((dic['Type3']!=None) or dic['Type3']!=""):
                    types=itemParamDescription.objects.filter(name__icontains=dic['Type3'].strip())
                    if(types.count()>0):
                        dic['Type3']=types[0].id
                    else:
                        temp_param={
                            "name":dic['Type3'],
                            "paramid":5,
                            "enabled":True,
                            "order":1
                        }
                        ser=itemParamDescriptionSerilizer(data=temp_param)
                        if(ser.is_valid()):
                            ser.save()
                            dic['Type3']=ser.data["id"]
                if 'ReasonsForNotFunctioning' in dic   and ((dic['ReasonsForNotFunctioning']!=None) or dic['ReasonsForNotFunctioning']!=""):
                    types=itemParamDescription.objects.filter(name__icontains=dic['ReasonsForNotFunctioning'].strip())
                    if(types.count()>0):
                        dic['ReasonsForNotFunctioning']=types[0].id
                    else:
                        temp_param={
                            "name":dic['ReasonsForNotFunctioning'],
                            "paramid":16,
                            "enabled":True,
                            "order":1
                        }
                        ser=itemParamDescriptionSerilizer(data=temp_param)
                        if(ser.is_valid()):
                            ser.save()
                            dic['ReasonsForNotFunctioning']=ser.data["id"]
                if 'FinancialSource' in dic   and ((dic['FinancialSource']!=None) or dic['FinancialSource']!=""):
                    types=itemParamDescription.objects.filter(name__icontains=dic['FinancialSource'].strip())
                    if(types.count()>0):
                        dic['FinancialSource']=types[0].id
                    else:
                        temp_param={
                            "name":dic['FinancialSource'],
                            "paramid":14,
                            "enabled":True,
                            "order":1
                        }
                        ser=itemParamDescriptionSerilizer(data=temp_param)
                        if(ser.is_valid()):
                            ser.save()
                            dic['FinancialSource']=ser.data["id"]
                if 'EnergySource_generator' in dic   and ((dic['EnergySource_generator']!=None) or dic['EnergySource_generator']!=""):
                    types=itemParamDescription.objects.filter(name__icontains=dic['EnergySource_generator'].strip())
                    if(types.count()>0):
                        dic['EnergySource_generator']=types[0].id
                    else:
                        temp_param={
                            "name":dic['EnergySource_generator'],
                            "paramid":13,
                            "enabled":True,
                            "order":1
                        }
                        ser=itemParamDescriptionSerilizer(data=temp_param)
                        if(ser.is_valid()):
                            ser.save()
                            dic['EnergySource_generator']=ser.data["id"]
                if 'PhysicalConditions' in dic   and ((dic['PhysicalConditions']!=None) or dic['PhysicalConditions']!=""):
                    types=itemParamDescription.objects.filter(name__icontains=dic['PhysicalConditions'].strip())
                    if(types.count()>0):
                        dic['PhysicalConditions']=types[0].id
                    else:
                        temp_param={
                            "name":dic['PhysicalConditions'],
                            "paramid":9,
                            "enabled":True,
                            "order":1
                        }
                        ser=itemParamDescriptionSerilizer(data=temp_param)
                        if(ser.is_valid()):
                            ser.save()
                            dic['PhysicalConditions']=ser.data["id"]
                if 'TechnicalConditions' in dic   and ((dic['TechnicalConditions']!=None) or dic['TechnicalConditions']!=""):
                    types=itemParamDescription.objects.filter(name__icontains=dic['TechnicalConditions'].strip())
                    if(types.count()>0):
                        dic['TechnicalConditions']=types[0].id
                    else:
                        temp_param={
                            "name":dic['TechnicalConditions'],
                            "paramid":10,
                            "enabled":True,
                            "order":1
                        }
                        ser=itemParamDescriptionSerilizer(data=temp_param)
                        if(ser.is_valid()):
                            ser.save()
                            dic['TechnicalConditions']=ser.data["id"]
                if 'IceMakingCapacity' in dic   and ((dic['IceMakingCapacity']!=None) or dic['IceMakingCapacity']!=""):
                    dic['IceMakingCapacity']=str(dic['IceMakingCapacity']).replace(",",".")
                    dic['IceMakingCapacity']=float(dic['IceMakingCapacity'])

                
                if 'CoolWaterProductionCapacity' in dic   and ((dic['CoolWaterProductionCapacity']!=None) or dic['CoolWaterProductionCapacity']!=""):
                    dic['CoolWaterProductionCapacity']=str(dic['CoolWaterProductionCapacity']).replace(",",".")
                    dic['CoolWaterProductionCapacity']=float(dic['CoolWaterProductionCapacity'])

                if 'OriginalCost' in dic   and ((dic['OriginalCost']!=None) or dic['OriginalCost']!=""):
                    dic['OriginalCost']=str(dic['OriginalCost']).replace(",",".")
                    dic["OriginalCost"]=int(float(dic["OriginalCost"]))

                if 'FreezerNetCapacity' in dic   and ((dic['FreezerNetCapacity']!=None) or dic['FreezerNetCapacity']!=""):
                    dic['FreezerNetCapacity']=str(dic['FreezerNetCapacity']).replace(",",".")
                    dic["FreezerNetCapacity"]=(float(dic["FreezerNetCapacity"]))
                if 'NetVaccineStorageCapacity' in dic   and ((dic['NetVaccineStorageCapacity']!=None) or dic['NetVaccineStorageCapacity']!=""):
                    dic['NetVaccineStorageCapacity']=str(dic['NetVaccineStorageCapacity']).replace(",",".")
                    dic["NetVaccineStorageCapacity"]=(float(dic["NetVaccineStorageCapacity"]))
                if 'NumberOfCoolantPacksRequired' in dic   and ((dic['NumberOfCoolantPacksRequired']!=None) or dic['NumberOfCoolantPacksRequired']!=""):
                    dic['NumberOfCoolantPacksRequired']=str(dic['NumberOfCoolantPacksRequired']).replace(",",".")
                    dic["NumberOfCoolantPacksRequired"]=(int(dic["NumberOfCoolantPacksRequired"]))
                if 'CoolantPackNominalCapacity' in dic   and ((dic['CoolantPackNominalCapacity']!=None) or dic['CoolantPackNominalCapacity']!=""):
                    dic['CoolantPackNominalCapacity']=str(dic['CoolantPackNominalCapacity']).replace(",",".")
                    dic["CoolantPackNominalCapacity"]=(float(dic["CoolantPackNominalCapacity"]))
                         
                dic['YearInstalled']=str(dic['YearInstalled'])

                if 'NotInUseSince' in dic and type(dic['NotInUseSince'])==str:
                    del dic['NotInUseSince']
                # print(dic)
                ser=itemSerializer(data=dic)
                if(ser.is_valid()):
                    ser.save()
                else:
                    res={
                        "error":ser.errors,
                        "counter":counter
                    }
                    return Response(res,status=status.HTTP_406_NOT_ACCEPTABLE)
                    
        return Response({"counter":counter},status=status.HTTP_200_OK)



class itemdbfix(APIView):
    def get(self,request):
        count=0
        items=item.objects.all()
        for i in items:
            # count+=1
            # # print(i.Manufacturer)
            # if(i.Manufacturer!=None):
            #     man=Manufacturer.objects.filter(id=i.Manufacturer)
            #     if(man.count()==0):
            #         i.Manufacturer="100"
            #         i.save()

            #     print(man.id)
            #     print(man.describe)
            # continue
            # love=Facility.objects.filter(parentid=i.id)

            # if(love.count()>=i.loverlevelfac):
            #     i.loverlevelfac=love.count()+1
            #     i.save()
            i.delete()
            count+=1

        return Response(count,status=status.HTTP_200_OK)


class itemDeleteView(APIView):
    def get(self,request):
        del_res=itemParamDescription.objects.filter(paramid=15,enabled=True)
        desc_ser=itemParamDescriptionSerilizer(del_res,many=True)
        return Response(desc_ser.data,status=status.HTTP_200_OK)
    def post(self,request):
        data=request.data
        print(data)
        id=data["id"]
        items=get_object_or_404(item,id=id)
        ser=itemSerializer(items,data=data)
        if(ser.is_valid()):
            ser.save()
            return Response(ser.data,status=status.HTTP_200_OK)
        print(ser.errors)    
        return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)    

class ItemAllfac(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        all_fac=Facility.objects.filter(parentid=request.user.facilityid.id)
        all_fac=Facility.objects.filter(id=request.user.facilityid.id)|all_fac
        items=item.objects.filter(facility__in=all_fac,isDel=False)
        ser=itemSerializer(items,many=True)
        new_data=copy.deepcopy(ser.data)
        for i in new_data:
                if(i["Manufacturer"] is not None):
                    man=get_object_or_404(Manufacturer,id=i["Manufacturer"])
                    i["Manufacturer"]=man.describe
                todo=toDoMaintance.objects.filter(item=i["id"])
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
                items=get_object_or_404(item,id=i["id"])
                mgp=maintancegp.objects.filter(id=items.MaintenanceGroup)
                if(mgp.count()>0):
                    mgp=mgp[0]
                    mgp=mgp.name
                else:
                    mgp=None
                final_ans={
                    "code":items.code,
                    "type": items.item_type.code+" - "+items.item_type.title,
                    "class":items.item_class.code+" - "+items.item_class.title,
                        "gp":mgp,
                        "maintanances":ans, 
                }    
                i["maintananceData"]=final_ans

        return Response(new_data,status=status.HTTP_200_OK)
class AllFieldView(APIView):
    def get(self,request):
        user=request.user
        facility=user.facilityid
        parent=request.query_params.get('parent',None)

        facility=get_object_or_404(Facility, id=facility.id)
        if(parent is not None and parent!=""):
            facility=get_object_or_404(Facility,id=parent)
            
        fac_ser=facilitySerializer(facility,many=False)
        level=facility.level.id
        levels_Ser=levelSerializer(level,many=True)
        item_type_id=[]
        itemTypeinlevels=Itemtypelevel.objects.filter(level=level,active=True)
        for x in itemTypeinlevels:
            item_type_id.append(x.itemtypeid.id)
        item_class=ItemClass.objects.filter(active=True)
        first_data=[]
        for item_C in item_class:
            x_ser=itemclassSerializer(x)
            item_type=ItemType.objects.filter(itemclass=item_C.id,active=True,id__in=item_type_id)
            second_data=[]
            for k in item_type:
                item_class=get_object_or_404(ItemClass,id=item_C.id)
                item_type=get_object_or_404(ItemType,id=k.id)
                Manufacturers=Manufacturer.objects.filter(active=True,itemclass=item_C.id)
                man_Ser=ManufacturerSerializer(Manufacturers,many=True)    
                related=relatedItemType.objects.filter(itemtype=item_type.id)
                related=related.order_by('id')
                fields=[]
                same_item={}
                same_item['field']={
                    "id":877,
                    "name":"Number of the same items with the same condition in this facility",
                    "params":[],
                    "required":False,
                    "state":"same_item",
                    "topic":"Other additional and optional fields",
                    "type":"number",
                    "validation":[
                        {
                            "id":877,
                            "digits":4,
                            "min":1,
                            "max":1000,
                            "float":False,
                            "floating":-1,
                            "fieldid":877,
                        }
                    ],
                }
                fields.append(same_item)
                for x in related:
                    data={}
                    field=Field.objects.get(id=x.field.id)
                    field_ser=fieldSerializer(field,many=False)
                    copys=copy.deepcopy(field_ser.data)
                    data["field"]=copys
                    data["field"]["required"]=x.required
                    if(field.id==2):
                    
                        data["field"]["params"]=man_Ser.data
                    else:
                        try:
                            param=itemParam.objects.get(fieldid=field.id)
                #    if(param.count()>0):
                            params=itemParamSerilizer(param,many=False)                        
                            describe=itemParamDescription.objects.filter(paramid=params.data["id"],enabled=True)
                            des_ser=itemParamDescriptionSerilizer(describe,many=True) 
                            data["field"]["params"]=des_ser.data
                #    else:
                        except:
                            data["field"]["params"]=[]    
                        if(field.id==76):
                            maint=maintancegp.objects.filter(enable=True,item_class=item_class.id,item_type=item_type.id)
                            maint_ser=maintancegpSerializers(maint,many=True)
                            data["field"]["params"]=maint_ser.data 
                        if(field.id==31):
                            data1= {
                        "id": 1,
                        "describe": "+25C",
                        "active": True,
                        "order": 1,
                        "itemclass": 1
                    }
                            data2= {
                        "id": 2,
                        "describe": "+2 - +8 C",
                        "active": True,
                        "order": 1,
                        "itemclass": 1
                    }
                            data3= {
                        "id": 3,
                        "describe": "-20 C",
                        "active": True,
                        "order": 1,
                        "itemclass": 1
                    }
                            data4={
                        "id": 4,
                        "describe": "-70 C",
                        "active": True,
                        "order": 1,
                        "itemclass": 1
                    }
                            data5={
                        "id": 5,
                        "describe": "Dry store",
                        "active": True,
                        "order": 1,
                        "itemclass": 1
                    }
                            ic_id=item_class.id
                            it_id=item_type.id
                            ans=[]
                            if(ic_id==1):
                                if(it_id==1 or it_id==3 or it_id==5):
                                    ans.append(data2)
                                elif(it_id==2 or it_id==4):
                                    ans.append(data3)
                                elif(it_id==6):
                                    ans.append(data4)
                                else:
                                    ans.append(data1)
                                    ans.append(data2)
                                    ans.append(data3)
                                    ans.append(data4)
                                    ans.append(data5)
                            else:
                                ans.append(data1)
                                ans.append(data2)
                                ans.append(data3)
                                ans.append(data4)
                                ans.append(data5)                    
                    
                    
                    
                    
                            data["field"]["params"]=ans


                            
                    val=Itemvalidation.objects.filter(fieldid=x.field.id)
                    val_ser=ItemvalidationSerilizer(val,many=True)

                    if(val.count()>0):
                        data["field"]["validation"]=val_ser.data
                    else:
                        data["field"]["validation"]=[]  
                    fields.append(data)
                #sort field by order
                fields=sorted(fields, key=lambda k: k['field']['id'])
                new_Data=[]
                if (k.havePQS):
                    if(item_C.code=='ACC'):
                        tcode=k.code
                    if(tcode=='REF' or tcode=='FRZ' or tcode=='CRF' or tcode=='UFR' or tcode=='IFR' ):
                        pqs=pqs3.objects.all()
                        ser=pqs3Serializer(pqs,many=True)
                        new_Data=copy.deepcopy(ser.data)
                        for i in new_Data:
                            i["ptype"]=3
                        
                    else:
                        pqss=pqs3.objects.all()
                        ser=pqs3Serializer(pqss,many=True)
                        new_Data=copy.deepcopy(ser.data)
                        for i in new_Data:
                            i["ptype"]=3
                        pqs44=pqs4.objects.all()
                        ser4=pqs4Serializer(pqs44,many=True)
                        new_Data4=copy.deepcopy(ser4.data)
                        for i in new_Data4:
                            i["ptype"]=4
                        new_Data=new_Data+new_Data4

                    if(item_C.code=='PCC'):
                        tcode=k.code
                        if(tcode=='CBX' or tcode=='VCX'):
                            pqs44=pqs4.objects.all()
                            ser4=pqs4Serializer(pqs44,many=True)
                            new_Data4=copy.deepcopy(ser4.data)
                            for i in new_Data4:
                                i["ptype"]=4
                            new_Data=new_Data4
                        else:
                            pqss=pqs3.objects.all()
                            ser=pqs3Serializer(pqss,many=True)
                            new_Data=copy.deepcopy(ser.data)
                            for i in new_Data:
                                i["ptype"]=3
                            pqs44=pqs4.objects.all()
                            ser4=pqs4Serializer(pqs44,many=True)
                            new_Data4=copy.deepcopy(ser4.data)
                            for i in new_Data4:
                                i["ptype"]=4
                            new_Data=new_Data+new_Data4
                    else:
                        pqss=pqs3.objects.all()
                        ser=pqs3Serializer(pqss,many=True)
                        new_Data=copy.deepcopy(ser.data)
                        for i in new_Data:
                            i["ptype"]=3
                        pqs44=pqs4.objects.all()
                        ser4=pqs4Serializer(pqs44,many=True)
                        new_Data4=copy.deepcopy(ser4.data)
                        for i in new_Data4:
                            i["ptype"]=4
                        new_Data=new_Data+new_Data4
    
                new_data_item={
                    "id":k.id,
                    "title":k.code+" - "+k.title,
                    "havepqs":k.havePQS,
                    "fields":fields,
                    "pqs":new_Data
                }
                second_data.append(new_data_item)
            data={
                "item_class":{
                    "id":item_C.id,
                    "title":item_C.code +" - " +item_C.title,

                },
                "item_type":second_data,
            }
            first_data.append(data)
        fac_data={
        "id":fac_ser.data["id"],
        "name":fac_ser.data["name"],
        "code":fac_ser.data["code"],
        "level":fac_ser.data["level"],
    }    
        ans={
            "facility":fac_data,
            "data":first_data
        } 
        return Response(ans)

class itemFixedView(APIView):

    def get(self,request):
        items=item.objects.all()
        for _copy in items:
            code=_copy.code
            code=code[:10]
            item_fac=_copy.facility.id
            code_fac=get_object_or_404(Facility,code=code)
            if(item_fac!=code_fac.id):
                _copy.facility=code_fac
                _copy.save()
        return Response("done")
