from django.urls import path
from .views import *


urlpatterns = [
    path('3', pqs3View.as_view(), name='pqs3 view'),
    path('4', pqs4View.as_view(), name='pqs4 view'),
 
    
]