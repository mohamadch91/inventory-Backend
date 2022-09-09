from operator import indexOf
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
        user=request.user
        user_ser=UserSerializer(user,many=False)
        this_facility=Facility.objects.filter(id=user.facilityid.id)[0]
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
        new_data["parentid"]=this_facility.id
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
        country = Facility.objects.filter(parentid=request.user.facilityid.id,is_deleted=False)
        country=Facility.objects.filter(id=request.user.facilityid.id)|country
        serializer =  facilitySerializer(country, many=True)
        ser_copy=copy.deepcopy(serializer.data)
        for i in (ser_copy):
            type=i["type"]
            if(type != None and type != ""):
                type_name=get_object_or_404(facilityParamDescription,id=type).name
                i["type"]=type_name
                

        return Response(ser_copy)

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
            return Response({"message": "Cannot delete facility with children"}, status=status.HTTP_409_CONFLICT)
        item_num=item.objects.filter(facility=facility.id).count()
        if item_num>0:
            return Response({"message": "Cannot delete facility with items"}, status=status.HTTP_409_CONFLICT)
        facility.delete()    
        return Response(status=status.HTTP_204_NO_CONTENT)

class facilityFieldView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        parent=request.query_params.get('parent',None)
        user=request.user
        user_ser=UserSerializer(user,many=False)
        this_facility=Facility.objects.filter(id=user.facilityid.id)[0]
        if(parent is not None):
            this_facility=get_object_or_404(Facility,id=parent)
        fac_ser=facilitySerializer(this_facility,many=False)
        country=get_object_or_404(CountryConfig,id=this_facility.country.id)
        parent_num=Facility.objects.filter(parentid=this_facility.id).count()
        parents=facilitySerializer(parent_num,many=True)
                    
        if(parent_num>= this_facility.loverlevelfac):
            print(parent_num)
            return Response("You have reached the maximum number of facilities you can add",status=status.HTTP_403_FORBIDDEN)


        level=this_facility.level
        allow_levels=LevelConfig.objects.filter(id__gt=level.id)
        counter=CountryConfig.objects.all()[0]
        allow_levels=allow_levels.filter(id__lte=counter.levels)
        if(allow_levels.count()==0):
            return Response ("you cannot add facility at this level",status=status.HTTP_403_FORBIDDEN)  
        
        levels_Ser=levelSerializer(allow_levels,many=True)
        rel=relatedFacility.objects.filter(active=True)
        ans=[]
        for x in rel:
            if(id==69):
                continue
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
            this=get_object_or_404(Facility,id=id)
            fac_Ser_this=facilitySerializer(this,many=False)
            final_ans=[]
            final_ans.append(fac_Ser_this.data)
            for x in fac_Ser.data:
                if(x["parentid"] is not None):
                    if(x["parentid"]==id):
                        final_ans.append(x)
            return Response(final_ans,status=status.HTTP_200_OK)
        return Response("need query param",status=status.HTTP_400_BAD_REQUEST)    
        

class importfacilityView(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self,request):
        ans=[]
        code=[]
        counter=0
        fac_count=Facility.objects.all()[len(Facility.objects.all())-1].id
        for x in request.data:
            data={}
            if(x["id"] is None):
                return Response("id is required",status=status.HTTP_406_NOT_ACCEPTABLE)
            if(x["code"] is None):
                return Response("code is required",status=status.HTTP_406_NOT_ACCEPTABLE)
            else:
                if(x["code"] in code):
                    return Response("code is not unique",status=status.HTTP_406_NOT_ACCEPTABLE)
                else:
                    code.append(x["code"])    
            if(x["name"] is None):
                return Response("name is required",status=status.HTTP_406_NOT_ACCEPTABLE)
            else:
                data["name"]=x["name"]    
            if(x["parentid"] is None):
                return Response(x["parentid"]+"parentid is required",status=status.HTTP_406_NOT_ACCEPTABLE)
            else:
                if(counter==0):
                    data["parentid"]=None
                    code.append(x["parentid"])
                else:
                    if(x["parentid"] not in code):
                        return Response(x["parentid"]+"parentid is not valid",status=status.HTTP_406_NOT_ACCEPTABLE)
                    i=code.index(x["parentid"])
                    data["parentid"]=i+fac_count
            typess=""        
            if(x["type"] is None):
                data["type"]=None
            else:
                type=x["type"]
                types=facilityParamDescription.objects.filter(paramid=10,enabled=True,name=type)
                if(types.count()==0):
                    return Response("type is not valid",status=status.HTTP_406_NOT_ACCEPTABLE)
                else:
                    data["type"]=types[0].id
            if((x["level"] is None and x["lname"] is None) or x["level"]==0):
                return Response("level is required",status=status.HTTP_406_NOT_ACCEPTABLE)
            else:
                if(x["level"] is None and x["lname"] is not None):
                    level=LevelConfig.objects.filter(name=x["lname"])
                    if(level.count()==0):
                        return Response("level is not valid",status=status.HTTP_406_NOT_ACCEPTABLE)
                    else:
                        data["level"]=level[0].id
                else:        
                    lcount=LevelConfig.objects.all().count()
                    if(x["level"]>lcount):
                        return Response("level is not valid",status=status.HTTP_406_NOT_ACCEPTABLE)
            
            if(x["pop"] is None):
                return Response("pop is required",status=status.HTTP_406_NOT_ACCEPTABLE)
            else:
                country=CountryConfig.objects.all()[0]
                level=LevelConfig.objects.filter(name=x["lname"])[0]
                if(x['pop']<level.minpop or x['pop']>level.maxpop):
                    return Response("pop is not valid",status=status.HTTP_406_NOT_ACCEPTABLE)
                if(country.poptarget=='General population'):
                    data['populationnumber']=int(x['pop'])
                else:
                    data['childrennumber']=int(x['pop'])    
            country=CountryConfig.objects.all()[0]
            country_code=country.codecountry
            level_code=data["level"]
            level_code =f"{level_code:02d}"
            facility_num=Facility.objects.filter(level=level_code)[len(Facility.objects.filter(level=level_code))-1].id
            facility_num=facility_num+1
            facility_num=f"{facility_num:05d}"
            data["code"]=f"{country_code}{level_code}{facility_num}"
            print(data["parentid"])
            ser=facilitySerializer(data=data)
            if(ser.is_valid()):
                ser.save()
                ns={}
                country=CountryConfig.objects.all()[0]
                level=LevelConfig.objects.filter(name=x["lname"])[0]
                if(x['pop']<level.minpop or x['pop']>level.maxpop):
                    return Response("pop is not valid",status=status.HTTP_406_NOT_ACCEPTABLE)
                if(country.poptarget=='General population'):
                    ns['pop']=int(x['pop'])
                else:
                    ns['pop']=int(x['pop']) 
                parent=""
                if(ser.data["parentid"] is not None):
                    parent=Facility.objects.filter(id=data["parentid"])[0].name
                type_ans=""
                if(ser.data["type"] is not None):
                    types=facilityParamDescription.objects.filter(paramid=10,enabled=True,name=ser.data["type"])[0].name    
                new_data={
                    "id":ser.data["id"],
                    "code":ser.data["code"],
                    "name":ser.data["name"],
                    "parentid":parent,
                    "type":type_ans,
                    "level":ser.data["level"],
                    "lname":level.name,
                    "pop":ns["pop"]

                }
                ans.append(new_data)
                counter=counter+1
            else:
                return Response(ser.errors,status=status.HTTP_406_NOT_ACCEPTABLE)
        return Response(ans,status=status.HTTP_200_OK)


                    
                
class testdb(APIView):
    def post(self,request):
        new_data=copy.deepcopy(request.data)
        for x in new_data:
            parent=None
            if(x["parent"] is not None):
                parent=Facility.objects.filter(name=x["parent"].strip())[0].id
            x["parentid"]=parent
            x.pop("parent")
            ser=facilitySerializer(data=x)
            if(ser.is_valid()):
                ser.save()
            else:
                return Response(ser.errors,status=status.HTTP_406_NOT_ACCEPTABLE)

        return Response("salam",status=status.HTTP_200_OK)        


class facilityFieldprintView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        parent=request.query_params.get('parent',None)
        user=request.user
        user_ser=UserSerializer(user,many=False)
        this_facility=Facility.objects.filter(id=user.facilityid.id)[0]
        if(parent is not None):
            this_facility=get_object_or_404(Facility,id=parent)
        fac_ser=facilitySerializer(this_facility,many=False)
        country=get_object_or_404(CountryConfig,id=this_facility.country.id)
        parent_num=Facility.objects.filter(parentid=this_facility.id).count()
        parents=facilitySerializer(parent_num,many=True)
                    
 
        level=this_facility.level
        allow_levels=LevelConfig.objects.filter(id__gt=level.id)
        counter=CountryConfig.objects.all()[0]
        allow_levels=allow_levels.filter(id__lte=counter.levels)
     
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

class facilityDeleteView(APIView):
    def get(self,request):
        del_res=facilityParamDescription.objects.filter(paramid=13,enabled=True)
        desc_ser=facilityParamDescriptionSerilizer(del_res,many=True)
        return Response(desc_ser.data,status=status.HTTP_200_OK)
    def post(self,request):
        data=request.data
        print(data)
        id=data["id"]
        facility = get_object_or_404(Facility, id=id)
        below=Facility.objects.filter(parentid=facility.id)
        if below.count()>0:
            return Response({"message": "Cannot delete facility with children"}, status=status.HTTP_409_CONFLICT)
        item_num=item.objects.filter(facility=facility.id).count()
        if item_num>0:
            return Response({"message": "Cannot delete facility with items"}, status=status.HTTP_409_CONFLICT)
        del_res=get_object_or_404(Facility,id=id)
        ser=facilitySerializer(data=del_res)
        if(ser.is_valid()):
            del_res.save()
            return Response(ser.data,status=status.HTTP_200_OK)
        return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)    


