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
from item.models import *
import copy
class FacilityView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        new_data=copy.deepcopy(request.data)
        country=CountryConfig.objects.all()[0]
        country_code=country.codecountry
        level_code=new_data["level"]
        level_code =f"{level_code:02d}"
        facility_num=Facility.objects.filter(level=level_code)[len(Facility.objects.filter(level=level_code))-1].id
        facility_num=facility_num+1
        facility_num=f"{facility_num:05d}"
        new_data["code"]=f"{country_code}{level_code}{facility_num}"
        new_data["country"]=country.id
        new_data["completerstaffname"]=request.user.id
        serializer =   facilitySerializer(data=new_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        id=request.query_params.get("id",None)
        if id is not None:
            facility = get_object_or_404(Facility, id=id)
            serializer = facilitySerializer(facility)
            return Response(serializer.data)
        country = Facility.objects.all()
        serializer =  facilitySerializer(country, many=True)
        return Response(serializer.data)

    def put(self, request, ):
        print(request)
        id=request.data["id"]
        country = get_object_or_404(Facility, id=id)
        serializer =  facilitySerializer(country, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        id=request.data["id"]
        facility = get_object_or_404(Facility, id=id)
        below=Facility.objects.filter(parentid=facility.id)
        if below.count()>0:
            return Response({"message": "Cannot delete facility with children"}, status=status.HTTP_400_BAD_REQUEST)
        item_num=item.objects.filter(facility=facility.id).count()
        if item_num>0:
            return Response({"message": "Cannot delete facility with items"}, status=status.HTTP_400_BAD_REQUEST)
        facility.delete()    
        return Response(status=status.HTTP_204_NO_CONTENT)

class facilityFieldView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        
        user=request.user
        user_ser=UserSerializer(user,many=False)
        this_facility=Facility.objects.filter(id=user.facilityid.id)[0]
        fac_ser=facilitySerializer(this_facility,many=False)
        country=get_object_or_404(CountryConfig,id=this_facility.country.id)
        parent_num=Facility.objects.all()
        parents=facilitySerializer(parent_num,many=True)
        counter=0
        for x in range(len(parents.data)):
            counter=0
            for y in range(x,len(parents.data)):
                # print(x,y)    
                if(parents.data[x]["parentid"] is not None):
                    if(parents.data[y]["parentid"] is not None):
                        if(parents.data[y]["parentid"]>=parents.data[x]["id"]):
                            # print("counter"+str(counter))
                            counter+=1
            if(parents.data[x]["loverlevelfac"] is not None):                
                if(counter>= parents.data[x]["loverlevelfac"]):
                    if(this_facility.id<parents.data[x]["id"]):
                        break
                    print(this_facility.id)        
                    print(parents.data[x]["id"])
                    print(parents.data[x]["loverlevelfac"])
                    print(counter)
                    return Response("You have reached the maximum number of facilities you can add",status=status.HTTP_403_FORBIDDEN)


        level=this_facility.level
        allow_levels=LevelConfig.objects.filter(id__gt=level.id)
        if(allow_levels.count()==0):
            return Response ("you cannot add facility at this level",status=status.HTTP_403_FORBIDDEN)  
        
        levels_Ser=levelSerializer(allow_levels,many=True)
        rel=relatedFacility.objects.filter(active=True)
        ans=[]
        for x in rel:
            if(x.id==1 or x.id ==3 or x.id==8 or x.id == 9 or x.id==10):
                continue
            if((x.id==6 or x.id==5) and country.poptarget=='General population'):
                if(x.id==5):
                    data={
                "id":x.id,
                "name":x.name,
                "topic":x.topic,
                "type":x.type,
                "active":x.active,
                "required":True,
                "stateName":x.state,
                "disabled":x.disabled,

                "params":[],
                     
                "validation":[{
                    "fieldid": 5,
                    "digits": -1,
                    "min": level.minpop,
                    "max": level.maxpop,
                    "float": False,
                    "floating": -1
                     }]

                    }
                else:
                      data={
                "id":x.id,
                "name":x.name,
                "topic":x.topic,
                "type":x.type,
                "active":x.active,
                "required":False,
                "stateName":x.state,
                "disabled":x.disabled,

                "params":[],
                     
                "validation":[{
                    "fieldid": 6,
                    "digits": -1,
                    "min": level.minpop,
                    "max": level.maxpop,
                    "float": False,
                    "floating": -1
                     }]

                    }

                ans.append(data)
                continue
            elif((x.id==6 or x.id==5) and country.poptarget=='Under-1 Population'):
                if(x.id==6):
                    data={
                "id":x.id,
                "name":x.name,
                "topic":x.topic,
                "type":x.type,
                "active":x.active,
                "required":True,
                "stateName":x.state,
                "disabled":x.disabled,

                "params":[],
                     
                "validation":[{
                    "fieldid": 6,
                    "digits": -1,
                    "min": level.minpop,
                    "max": level.maxpop,
                    "float": False,
                    "floating": -1
                     }]

                    }
                else:
                      data={
                "id":x.id,
                "name":x.name,
                "topic":x.topic,
                "type":x.type,
                "active":x.active,
                "required":False,
                "stateName":x.state,
                "disabled":x.disabled,

                "params":[],
                     
                "validation":[{
                    "fieldid": 5,
                    "digits": -1,
                    "min": level.minpop,
                    "max": level.maxpop,
                    "float": False,
                    "floating": -1
                     }]

                    }    
                ans.append(data)
                continue   
            param=facilityParam.objects.filter(fieldid=x.id).order_by('order')
            desc_ser=[]
            
            for y in param:
                desc=facilityParamDescription.objects.filter(paramid=y.id).order_by('order')
                desc_ser=facilityParamDescriptionSerilizer(desc,many=True)
            data={}    
            if(desc_ser==[]):
                     data={
                "id":x.id,
                "name":x.name,
                "topic":x.topic,
                "type":x.type,
                "active":x.active,
                "required":x.required,
                "stateName":x.state,
                "disabled":x.disabled,

                "params":[]
                     }
            else:         
                data={
                    "id":x.id,
                    "name":x.name,
                    "topic":x.topic,
                    "type":x.type,
                    "active":x.active,
                    "required":x.required,
                    "stateName":x.state,
                    "disabled":x.disabled,
                    "params":desc_ser.data
                }
            val=Facilityvalidation.objects.filter(fieldid=x.id)
            val_ser=FacilityvalidationSerilizer(val,many=True)
            if(val.count()>0):
                data["validation"]=val_ser.data
            else:
                data["validation"]=[]    

            ans.append(data)
        fac_data={
            "id":fac_ser.data["id"],
            "name":fac_ser.data["name"]
        }
        user_data={
            "id":user_ser.data["pk"],
            "username":user_ser.data["username"]
        }    
        data={
            "facility":fac_data,
            "user":user_data,
            "levels":levels_Ser.data,
            "related":ans
        }
        return Response(data,status=status.HTTP_200_OK)




class facilityPArentView(APIView):
    def get(self,request):
        id=request.query_params.get('id',None)
        if(id is not None):
            id=int(id)
            fac=Facility.objects.all()
            fac_Ser=facilitySerializer(fac,many=True)
            final_ans=[]
            for x in fac_Ser.data:
                if(x["parentid"] is not None):
                    if(x["parentid"]>=id):
                        final_ans.append(x)
            return Response(final_ans,status=status.HTTP_200_OK)
        return Response("need query param",status=status.HTTP_400_BAD_REQUEST)    
        

