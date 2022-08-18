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


class languageView(APIView):
    def get(self,request):
        name=request.query_params.get('name',None)
        if name is not None:
            lang = languages.objects.filter(name=name)
            words=words.objects.filter(language=lang.id)
            serializer =  languageWordSerializer(lang, many=True)
            ans={
                "language":lang.name,
                "words":serializer.data,
            }
            return Response(ans)
        else:
            lang=languages.objects.all()
            ans=[]
            for x in lang:
                words=words.objects.filter(language=x.id)
                serializer =  languageWordSerializer(x, many=True)
                ans.append({
                    "language":x.name,
                    "words":serializer.data,
                })
            return Response(ans)    