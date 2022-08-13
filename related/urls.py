from django.urls import path
from .views import *


urlpatterns = [
    path('related-facility/', relatedfacilityView.as_view(), name='related facility view'),
 
    
]