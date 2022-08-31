
from django.urls import path
from .views import *


urlpatterns = [

    path('item', dashboarditemView.as_view(), name='item'),
    path('facility', dashboardFacilityView.as_view(), name='facility'),
    path('table', dahboardlevelView.as_view(), name='table'),
    path('maintenance', getitemmaintatnce.as_view(), name='table'),
    path('todo', todoMaintances.as_view(), name='todo'),
    #add defined log view
    path('maintenancelog', definedlogView.as_view(), name='log'),





  
    
]