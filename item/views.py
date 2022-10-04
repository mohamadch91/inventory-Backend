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
        deleted=request.query_params.get('deleted',False)
        if(facility is not None):
            country=item.objects.filter(facility=facility,isDel=False)
            serializer =  itemSerializer(country, many=True)
            new_data=copy.deepcopy(serializer.data)
            for i in new_data:
                if(i["Manufacturer"] is not None):
                    man=get_object_or_404(Manufacturer,id=i["Manufacturer"])
                    i["Manufacturer"]=man.describe
            return Response(new_data)
        if(id is not None):    
            country = item.objects.filter(id=id,isDel=False)
            serializer =  itemSerializer(country, many=True)
            new_data=copy.deepcopy(serializer.data)
            return Response(new_data)
        if(deleted=="true"):
            country = item.objects.filter(facility=request.user.facilityid,isDel=True) 
        else:
            country = item.objects.filter(facility=request.user.facilityid,isDel=False) 
        serializer =  itemSerializer(country, many=True)
        new_data=copy.deepcopy(serializer.data)
        for i in new_data:
            if(i["Manufacturer"] is not None):
                man=get_object_or_404(Manufacturer,id=i["Manufacturer"])
                i["Manufacturer"]=man.describe
        return Response(new_data)

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
            "name":fac_ser.data["name"],
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
            "name":fac_ser.data["name"],
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
                if(tcode=='CBX' or tcode=='VBX'  ):
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
                    
            return Response("need query param",status=status.HTTP_200_OK)

            
class itemdb(APIView):
    def post(self,request):
        new_data=copy.deepcopy(request.data)
        for i in new_data:
            fac=get_object_or_404(Facility,code=i["facility"])
            i["facility"]=fac.id
            item_type=get_object_or_404(ItemType,title=i["item_type"])
            i["item_type"]=item_type.id
            item_class=get_object_or_404(ItemClass,title=i["item_class"])
            i["item_class"]=item_class.id
            if(i["StorageCondition"]=="2-8 C"):
                i["StorageCondition"]="+2 - +8 C"
            if(i["StorageCondition"]=="-20 C"):
                i["StorageCondition"]="-20 C"
            if(i["StorageCondition"]=="-70 C"):
                i["StorageCondition"]="-70 C"   
            ser=itemSerializer(data=i)     
            if ser.is_valid():
                ser.save()
            else:
                return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)
        
        return Response("ok",status=status.HTTP_200_OK)

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


