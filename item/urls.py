from django.urls import path
from .views import *



urlpatterns = [

      path('item-field', itemFieldView.as_view(), name='item-field'),
     path('', itemView.as_view(), name='item'),   
     path('itempqs', itemPQSView.as_view(), name='item'),   
     path('db', itemdb.as_view(), name='item'),   
      path('delete', itemDeleteView.as_view(), name='item import with excel '),
      path('itemallFac', ItemAllfac.as_view(), name='item import with excel '),
]