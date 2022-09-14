from copy import copy
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
from .serializers import *
from rest_framework.permissions import IsAuthenticated

from authen.models import User
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
import copy

# Create your views here.
class relatedfacilityView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self,request):
        query_set=relatedFacility.objects.all()
        serializer = relatedfacilitySerilizer(query_set, many=True)
        new_data=copy.deepcopy(serializer.data)
        country=CountryConfig.objects.all()[0]
        if(country.poptarget is not None):
            if(country.poptarget == 'General population'):
                new_data[4]['required']=True
                new_data[5]['required']=False

            else:
                new_data[5]['required']=True
                new_data[4]['required']=False

        return Response(new_data)
    def put(self, request):
        ans=[]
        for x in request.data:
            id=x["id"]
            print(type(id))
            if(id==35):
                for i in range(2):
                    country = get_object_or_404(relatedFacility, id=id+i+1)
                    
                    data={
                        "id":i+1,
                        "active":x["active"],
                        "required":x["required"],
                         "name":country.name,
                        "type":country.type

                    }
                    serializer = relatedfacilitySerilizer(country, data=data)
                    if serializer.is_valid():
                        serializer.save()
                        ans.append(serializer.data)
                    else:
                        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            if(id==38):
                for i in range(9):
                    
                    country = get_object_or_404(relatedFacility, id=id+i+1)
                    data={
                        "id":i+1,
                        "active":x["active"],
                        "required":x["required"],
                        "name":country.name,
                        "type":country.type

                    }
                    serializer = relatedfacilitySerilizer(country, data=data)
                    if serializer.is_valid():
                        serializer.save()
                        ans.append(serializer.data)
                    else:
                        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            if(id==48):
                for i in range(1):
                   
                    country = get_object_or_404(relatedFacility, id=id+i+1)
                    data={
                        "id":i+1,
                        "active":x["active"],
                        "required":x["required"],
                        "name":country.name,
                        "type":country.type

                    }
                    serializer = relatedfacilitySerilizer(country, data=data)
                    if serializer.is_valid():
                        serializer.save()
                        ans.append(serializer.data)    
                    else:
                        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
            if(id==50):
                for i in range(1):

                    country = get_object_or_404(relatedFacility, id=id+i+1)
                    data={
                        "id":i+1,
                        "active":x["active"],
                        "required":x["required"],
                        "name":country.name,
                        "type":country.type

                    }
                    serializer = relatedfacilitySerilizer(country, data=data)
                    if serializer.is_valid():
                        serializer.save()
                        ans.append(serializer.data)    
                    else:
                        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

                
            country = get_object_or_404(relatedFacility, id=id)
            serializer = relatedfacilitySerilizer(country, data=x)
            if serializer.is_valid():
                serializer.save()
                ans.append(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(ans)    
class fieldView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self,request):
        query_set=Field.objects.all()
        query_set=query_set.exclude(id=59)
        query_set=query_set.exclude(id=60)
        query_set=query_set.exclude(id=81)

        query_set=query_set.exclude(id=61)

        query_set=query_set.exclude(id=62)
        query_set=query_set.exclude(id=63)

        serializer = fieldSerializer(query_set, many=True)
        return Response(serializer.data)    
    def put(self,request):
        print(request.data)
        id=request.data["id"]
        country = get_object_or_404(Field, id=id)
        serializer = fieldSerializer(country, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class relatedItemTypeView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self,request):
        id=request.query_params.get('id', None)
        ans=None
        if(id==None):
            query_set=relatedItemType.objects.all()
            serializer = relatedItemTypeSerilizer(query_set, many=True)
            ans=serializer.data
        else:
            itemType=get_object_or_404(ItemType, id=id)
            query_set=relatedItemType.objects.filter(itemtype=itemType)
            serializer = relatedItemTypeSerilizer(query_set, many=True)
            ans=serializer.data
        final_ans=[]    
        for x in ans:
            field=get_object_or_404(Field, id=x['field'])
            itemtype=get_object_or_404(ItemType, id=x['itemtype'])
            field_serilize=fieldSerializer(field)
            itemtype_serilize=itemtypeSerializer(itemtype)
            x['field']=field_serilize.data
            x['itemtype']=itemtype_serilize.data
            final_ans.append(x)
        return Response(final_ans,status=status.HTTP_200_OK)    

    def put(self,request):
        ans=[]
        for x in request.data:
            enable=x['enable']
            if(enable):
                field=get_object_or_404(Field, id=x['fieldid'])
                itemtype=get_object_or_404(ItemType, id=x['itemtypeid'])
                obj=relatedItemType.objects.filter(field=x['fieldid'], itemtype=x['itemtypeid'])
                if(len(obj)==0):
                    if(field.id==25):
                        for i in range(1,3):
                            data={
                                "field":field.id+i,
                                "itemtype":itemtype.id,
                                "required":x['required']
                            }
                            serializer = relatedItemTypeSerilizer(data=data)
                            if serializer.is_valid():
                                serializer.save()
                                ans.append(serializer.data)
                    data={
                        'field':field.id,
                        'itemtype':itemtype.id ,
                        'required':x['required']
                    }
                    serializer = relatedItemTypeSerilizer(data=data)
                    if serializer.is_valid():
                        serializer.save()
                        ans.append(serializer.data)
                    else:
                        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                else:
                    obj=relatedItemType.objects.filter(field=x['fieldid'], itemtype=x['itemtypeid'])
                    obj.update(required=x['required'])
                    # data={
                    #     "required":x['required'],
                    #     "itemtype":itemtype.id,
                    #     "field":field.id
                    # }
                    # ser=relatedItemTypeSerilizer(obj, data=data)
                    # if ser.is_valid():
                    #     ser.save()
                    #     ans.append(ser.data)
                    # else:
                    #     return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
                        
            else:
                if(x['fieldid']==25):
                    obj=relatedItemType.objects.filter(field=x['fieldid']+1, itemtype=x['itemtypeid'])
                    obj.delete()
                    obj=relatedItemType.objects.filter(field=x['fieldid']+2, itemtype=x['itemtypeid'])
                    obj.delete()
                
                obj=relatedItemType.objects.filter(field=x['fieldid'], itemtype=x['itemtypeid'])
                if(len(obj)==1):
                    obj.delete()
        return Response(ans,status=status.HTTP_200_OK)



class paramView(APIView):
    # permission_classes = (IsAuthenticated,)
    def get(self,request):
        id=request.query_params.get('id', None)
        type=request.query_params.get('type', None)
        if(id==None):
            facility=[]
            item=[]
            facility_param=facilityParam.objects.all()
            item_param=itemParam.objects.all()
            for x in facility_param:
                field=get_object_or_404(relatedFacility, id=x.fieldid.id)
                field_ser=relatedfacilitySerilizer(field)
                name=field_ser.data['name']
                description=facilityParamDescription.objects.filter(paramid=x.id)
                description_ser=facilityParamDescriptionSerilizer(description, many=True)
                ans={
                    "id":x.id,
                    "name":name,
                    "order":x.order,
                    "description":len(description_ser.data)
                }
                facility.append(ans)
            for x in item_param:
                field=get_object_or_404(Field, id=x.fieldid.id)
                field_ser=fieldSerializer(field)
                name=field_ser.data['name']
                description=itemParamDescription.objects.filter(paramid=x.id)
                description_ser=itemParamDescriptionSerilizer(description, many=True)
                ans={
                    "id":x.id,
                    "name":name,
                    "order":x.order,
                    "description":len(description_ser.data)
                }
                item.append(ans)    
            final_ans={
                "facility":facility,
                "item":item
            }
            return Response(final_ans,status=status.HTTP_200_OK)
        else:
            if(type=='facility'):
                description=facilityParamDescription.objects.filter(paramid=id)
                description_ser=facilityParamDescriptionSerilizer(description, many=True)
                facility_param=facilityParam.objects.filter(id=id)[0]
                field=get_object_or_404(relatedFacility, id=facility_param.fieldid.id)
                field_ser=relatedfacilitySerilizer(field)
                new_data={
                    "name":field_ser.data['name'],
                    "description":description_ser.data

                }
                return Response(new_data,status=status.HTTP_200_OK)
            else:
                description=itemParamDescription.objects.filter(paramid=id)
                description_ser=itemParamDescriptionSerilizer(description, many=True)
                facility_param=itemParam.objects.filter(id=id)[0]
                field=get_object_or_404(Field, id=facility_param.fieldid.id)
                field_ser=fieldSerializer(field)
                new_data={
                    "name":field_ser.data['name'],
                    "description":description_ser.data

                }
                return Response(new_data,status=status.HTTP_200_OK)    

            

    def put(self,request):
        if( 'id' not in request.data):
                type=request.data['type']
                ans=[]
                if(type=='facility'):
                    ser=facilityParamDescriptionSerilizer(data=request.data)
                    if ser.is_valid():
                        ser.save()
                        ans.append(ser.data)
                    else:
                        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
                else:
                    ser=itemParamDescriptionSerilizer(data=request.data)
                    if ser.is_valid():
                        ser.save()
                        ans.append(ser.data)
                    else:
                        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
                return Response(ans,status=status.HTTP_200_OK)
        else:
            id=request.data['id']
            type=request.data['type']
            ans=[]
            if(type=='facility'):
                obj=get_object_or_404(facilityParamDescription, id=id)
                ser=facilityParamDescriptionSerilizer(obj, data=request.data)
                if ser.is_valid():
                    ser.save()
                    ans.append(ser.data)
                else:
                    return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                obj=get_object_or_404(itemParamDescription, id=id)
                ser=itemParamDescriptionSerilizer(obj, data=request.data)
                if ser.is_valid():
                    ser.save()
                    ans.append(ser.data)
                else:
                    return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response(ans,status=status.HTTP_200_OK)                        
                        

