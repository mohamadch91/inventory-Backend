from django.urls import path
from .views import *


urlpatterns = [

    path('helper', helperView.as_view(), name='Itemclass'),
    path('', maintananceView.as_view(), name='Itemtype'),
    
]