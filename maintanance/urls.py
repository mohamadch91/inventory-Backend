from django.urls import path
from .views import *


urlpatterns = [

    path('helper', helperView.as_view(), name='mhelper'),
    path('', maintananceView.as_view(), name='maintance'),
    path('active', activemainView.as_view(), name='active'),
    
    
]