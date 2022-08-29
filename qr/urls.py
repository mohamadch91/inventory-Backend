
from django.urls import path
from .views import *


urlpatterns = [

    path('helper', QRhelperview.as_view(), name='helper'),




  
    
]