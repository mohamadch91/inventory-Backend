from django.urls import path
from .views import *


urlpatterns = [

    path('itemClass', itemclassView.as_view(), name='Itemclass'),
    path('itemType', itemtypeView.as_view(), name='Itemtype'),
  
    
]