from django.urls import path
from .views import *


urlpatterns = [
    path('country/', CountryView.as_view(), name='country view'),
    path('level',LevelView.as_view(), name='level view'),
    path('country/', CountryView.as_view(), name='country view'),
    path('level/',LevelView.as_view(), name='level view'),
    
]