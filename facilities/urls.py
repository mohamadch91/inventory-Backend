from django.urls import path
from .views import *


urlpatterns = [

    path('facility-field', facilityFieldView.as_view(), name='facility-field'),
    path('', FacilityView.as_view(), name='facility'),
    path('parent', facilityPArentView.as_view(), name='facility '),
    path('import', importfacilityView.as_view(), name='facility import with excel '),


  
    
]