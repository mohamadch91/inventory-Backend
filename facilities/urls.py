from django.urls import path
from .views import *


urlpatterns = [

    path('facility-field', facilityFieldView.as_view(), name='facility-field'),
    path('', FacilityView.as_view(), name='facility'),

  
    
]