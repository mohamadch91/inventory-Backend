from django.urls import path
from .views import *


urlpatterns = [

    path('', HelpView.as_view(), name='help manage'),

  
    
]