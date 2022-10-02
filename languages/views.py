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
            pnum=int(pnum) 
            lang = languages.objects.filter(name=name)[0]
            
            words=languages_words.objects.filter(language=lang.id)
            if(search is not None):
                words=languages_words.objects.filter(language=lang.id,word__icontains=search) or languages_words.objects.filter(language=lang.id,translate__icontains=search)
            serializer =  languageWordSerializer(words, many=True)
            
            ans={
                "language":lang.name,
                "words":serializer.data[((pnum-1)*20):(pnum*20)],
            }
            return Response(ans)
        else:
            lang=languages.objects.all()
            ans=[]
            for x in lang:

                words=languages_words.objects.filter(language=x.id)
                if(search is not None):
                     words=languages_words.objects.filter(language=x.id,word__icontains=search) or languages_words.objects.filter(language=x.id,translate__icontains=search)
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
            lang=languages.objects.all()
            final_ans=[]
            ids=[]
            for x in lang:
                lang_words=languages_words.objects.filter(language=x.id)
                dict={}
                if(lang_words.count()==0):
                    continue
                else:
                    ids.append(x.id)
                    for k in lang_words:
                        print(k)
                        dict[k.word]=k.translate
                
                final_ans.append(dict)
            counter=1    
            for i in range(len(ids)):
                lang=languages.objects.filter(id=ids[i])[0]
               
                json_obj=json.dumps(final_ans[i],indent=4)
                print(lang.name)
                counter+=1
                # with open('./media/'+lang.name+'/translation.json', "w") as outfile:
                #     outfile.write(json_obj)      
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def put(self, request):
        id=request.data["id"]
        lang = get_object_or_404(languages_words, id=id)
        serializer =  languageWordSerializer(lang, data=request.data)
        if serializer.is_valid():
            serializer.save()
            lang=languages.objects.all()
            final_ans=[]
            ids=[]
            for x in lang:
                lang_words=languages_words.objects.filter(language=x.id)
                dict={}
                if(lang_words.count()==0):
                    continue
                else:
                    ids.append(x.id)
                    for k in lang_words:
                        # print(k)
                        dict[k.word]=k.translate
                 
                final_ans.append(dict)
            counter=1    
            for i in range(len(ids)):
                json_obj=json.dumps(final_ans[i],indent=4)
                lang=languages.objects.filter(id=ids[i])[0]
                counter+=1
                # print(lang.name)
                # with open('./media/'+lang.name+'/translation.json', "w") as outfile:
                #     outfile.write(json_obj)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request):
        id=request.data["id"]
        lang = get_object_or_404(languageWordSerializer, id=id)
        lang.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    

class getlanguages(APIView):
    def get(self,request):
        print(request)
        name=request.query_params.get('name',None)
        lang = get_object_or_404(languages,name=name)
        
        words=languages_words.objects.filter(language=lang.id)
        ans={}
        for i in words:
            if(i.word !=""):
                ans[i.word]=i.translate
        
        
        return Response(ans)
        