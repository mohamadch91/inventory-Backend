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