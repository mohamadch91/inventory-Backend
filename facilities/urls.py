from django.urls import path
from .views import *


urlpatterns = [

    path('', FacilityView.as_view(), name='facility view'),
  
    
]