
from django.urls import path
from .views import *


urlpatterns = [

    path('helper', QRhelperview.as_view(), name='helper'),
    path('list', generateQrView.as_view(), name='list'),
    path('getqr', getqrView.as_view(), name='get qr'),
    




  
    
]