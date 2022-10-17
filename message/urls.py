from django.urls import path
from .views import *


urlpatterns = [

    path('', messageView.as_view(), name='message'),
    path('helper', messageView.as_view(), name='message'),


  
    
]