from typing import final
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
        facility=new_data["facility"]
        facility=get_object_or_404(Facility, id=facility)
        item_class=new_data["item_class"]
        item_type=new_data["item_type"]
        item_class=get_object_or_404(ItemClass, id=item_class)
        item_type=get_object_or_404(ItemType, id=item_type)   
        item_code=f"{item.objects.all()[item.objects.count()-1].id+1:03d}"    
        new_data["code"]=f"{facility.code}{item_class.code}{item_type.code}{item_code}"
        serializer = itemSerializer(data=new_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        id=request.query_params.get('id',None)
        if(id is not None):
                
            country = item.objects.filter(id=id)
            serializer =  itemSerializer(country, many=True)
            return Response(serializer.data)

        country = item.objects.all()
        serializer =  itemSerializer(country, many=True)
        return Response(serializer.data)

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
        if class_id is None and type_id is None:
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
                    new_data={
                        "id":k.id,
                        "title":k.title,
                        "havepqs":k.havePQS,
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
            fac_data={
            "id":fac_ser.data["id"],
            "name":fac_ser.data["name"]
        }    
            ans={
                "facility":fac_data,
                "data":first_data
            }    
            return Response(ans)
        else:
            item_class=get_object_or_404(ItemClass,id=class_id)
            item_type=get_object_or_404(ItemType,id=type_id)
            ans={}
            Manufacturers=Manufacturer.objects.filter(active=True,itemclass=item_class.id)
            man_Ser=ManufacturerSerializer(Manufacturers,many=True)    
            related=relatedItemType.objects.filter(itemtype=item_type.id)
            fields=[]
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
                        ans=[

    {
                    "id": 1,
                    "describe": "+25C",
                    "active": True,
                    "order": 1,
                    "itemclass": 1
                },
                {
                    "id": 2,
                    "describe": "+2 - +8 C",
                    "active": True,
                    "order": 1,
                    "itemclass": 1
                },
                      {
                    "id": 3,
                    "describe": "-20 C",
                    "active": True,
                    "order": 1,
                    "itemclass": 1
                },
                      {
                    "id": 4,
                    "describe": "-70 C",
                    "active": True,
                    "order": 1,
                    "itemclass": 1
                },
                      {
                    "id": 5,
                    "describe": "Dry store",
                    "active": True,
                    "order": 1,
                    "itemclass": 1
                },



                        ]
                        data["field"]["params"]=ans


                         
                val=Itemvalidation.objects.filter(fieldid=x.id)
                val_ser=ItemvalidationSerilizer(val,many=True)
                if(val.count()>0):
                    data["field"]["validation"]=val_ser.data
                else:
                    data["field"]["validation"]=[]     
                fields.append(data)
            return Response(fields)       



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
                    return Response(ser.data,status=status.HTTP_200_OK)
                else:
                    pqss=pqs3.objects.all()
                    ser=pqs3Serializer(pqss,many=True)
                    pqs44=pqs4.objects.all()
                    ser4=pqs4Serializer(pqs44,many=True)
                    ans=ser4.data +ser.data 
                    return Response(ans,status=status.HTTP_200_OK)       

            if(item_class.code=='PCC'):
                tcode=item_type.code
                if(tcode=='CBX' or tcode=='VBX'  ):
                    pqs44=pqs4.objects.all()
                    ser4=pqs4Serializer(pqs44,many=True)
                    return Response(ser4.data,status=status.HTTP_200_OK)
                else:
                    pqss=pqs3.objects.all()
                    ser=pqs3Serializer(pqss,many=True)
                    pqs44=pqs4.objects.all()
                    ser4=pqs4Serializer(pqs44,many=True)
                    ans=ser4.data +ser.data 
                    return Response(ans,status=status.HTTP_200_OK)       
            else:
                pqss=pqs3.objects.all()
                ser=pqs3Serializer(pqss,many=True)
                pqs44=pqs4.objects.all()
                ser4=pqs4Serializer(pqs44,many=True)
                ans=ser4.data +ser.data 
                return Response(ans,status=status.HTTP_200_OK)   
        else:
                    
            return Response("need query param",status=status.HTTP_200_OK)

            

        