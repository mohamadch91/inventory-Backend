from django.shortcuts import render

# Create your views here.

from copy import copy
from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
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

from facilities.serializers import facilitySerializer

# Create your views here.
from .serializers import *
from rest_framework.permissions import IsAuthenticated

from authen.models import User
from .models import *
from .serializers import *
from settings.serializers import *
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from facilities.models import *
import copy

class messageView(APIView):
    def get(self,request):
        type=request.query_params.get('type',None)
        user=request.user
        facility=Facility.objects.filter(id=user.facilityid.id)[0]
        if (type=="sender"):
            messages=messageSerializer(message.objects.filter(sender=facility.id),many=True)
            final_ans=[]
            for x in messages.data:
                ans=copy.deepcopy(x)
                send_fac=get_object_or_404(Facility,id=x["sender"])
                sender={
                    "id":send_fac.id,
                    "name":send_fac.name
                }
                recv_fac=get_object_or_404(Facility,id=x["reciever"])
                reciev={
                    "id":recv_fac.id,
                    "name":recv_fac.name
                }
                ans["sender"]=sender
                ans["reciever"]=reciev
                final_ans.append(ans)
            return Response(final_ans)
        else:
            m=message.objects.filter(reciever=facility.id)
            messages=messageSerializer(m,many=True)
            messages=messageSerializer(message.objects.filter(reciever=facility.id),many=True)
            final_ans=[]
            for x in messages.data:
                ans=copy.deepcopy(x)
                send_fac=get_object_or_404(Facility,id=x["sender"])
                sender={
                    "id":send_fac.id,
                    "name":send_fac.name
                }
                recv_fac=get_object_or_404(Facility,id=x["reciever"])
                reciev={
                    "id":recv_fac.id,
                    "name":recv_fac.name
                }
                ans["sender"]=sender
                ans["reciever"]=reciev
                final_ans.append(ans)
            return Response(final_ans)
    def post(self, request):
        new_data=copy.deepcopy(request.data)
        user=request.user
        facility=Facility.objects.filter(id=user.facilityid.id)[0]
        new_data["sender"]=facility.id
        recievers=request.data["reciever"]
        ans=[]
        for x in recievers:
            new_data["reciever"]=x
            serializer =  messageSerializer(data=new_data)
            if serializer.is_valid():
                serializer.save()
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            ans.append(serializer.data)
        return Response(ans,status=status.HTTP_200_OK)
    def put(self, request):
        id=request.data["id"]
        messages = get_object_or_404(message, id=id)
        serializer =  messageSerializer(messages, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request):
        id=request.data["id"]
        messages = get_object_or_404(message, id=id)
        messages.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class helperView(APIView):
    permission_classes= [IsAuthenticated]
    def get(self,request):
        facility=Facility.objects.filter(parentid=request.user.facilityid.id,is_deleted=False)
        facility=Facility.objects.filter(id=request.user.facilityid.id)|facility
        parent=request.user.facilityid.parentid
        if(parent is not None):
            facility=Facility.objects.filter(id=request.user.facilityid.parentid.id)|facility
        ans=[]
        for x in facility:
            data={
                "id":x.id,
                "name":x.name
            }
            ans.append(data)
        ans=sorted(ans, key = lambda i: i['id'])
        return Response(ans)