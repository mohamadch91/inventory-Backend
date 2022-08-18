from django.urls import path
from .views import *


urlpatterns = [

      path('item-field', itemFieldView.as_view(), name='item-field'),
     path('', itemView.as_view(), name='item'),

  
  
    
]