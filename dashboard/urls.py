
from django.urls import path
from .views import *


urlpatterns = [

    path('item', dashboarditemView.as_view(), name='item'),
    path('facility', dashboardFacilityView.as_view(), name='facility'),
    path('table', dahboardlevelView.as_view(), name='table'),
    path('maintance', getitemmaintatnce.as_view(), name='table'),





  
    
]