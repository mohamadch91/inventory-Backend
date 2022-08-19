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

class languageView(APIView):
    def get(self,request):
        name=request.query_params.get('name',None)
        pnum=request.query_params.get('pnum',None),
        search=request.query_params.get('search',None)
        pnum=pnum[0]
        
        if name is not None:
            if(pnum is None):
                    return Response("need query page num")
            pnum=int(pnum[0]) 
            lang = languages.objects.filter(name=name)[0]
            
            words=languages_words.objects.filter(language=lang.id)
            if(search is not None):
                words=languages_words.objects.filter(language=lang.id,word__contains=search) or languages_words.objects.filter(language=lang.id,translate__contains=search)
            serializer =  languageWordSerializer(words, many=True)
            serializer.data[(pnum-1)*20:pnum*20]
            ans={
                "language":lang.name,
                "words":serializer.data,
            }
            return Response(ans)
        else:
            print("salam")
            lang=languages.objects.all()
            ans=[]
            for x in lang:

                words=languages_words.objects.filter(language=x.id)
                if(search is not None):
                     words=languages_words.objects.filter(language=x.id,word__contains=search) or languages_words.objects.filter(language=x.id,translate__contains=search)
                z=words.count()

                ans.append({
                    "language":x.name,
                    "words":z
                })
            return Response(ans)    
    def post(self,request):
        new_data=copy.deepcopy(request.data)
        lang=request.data["language"]
        lang=languages.objects.get(name=lang)
        new_data["language"]=lang.id
        serializer =  languageWordSerializer(data=new_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def put(self, request):
        id=request.data["id"]
        lang = get_object_or_404(languages_words, id=id)
        serializer =  languageWordSerializer(lang, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request):
        id=request.data["id"]
        lang = get_object_or_404(languageWordSerializer, id=id)
        lang.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    