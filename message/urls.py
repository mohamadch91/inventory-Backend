from django.urls import path
from .views import *


urlpatterns = [

    path('', messageView.as_view(), name='message'),
    path('helper', helperView.as_view(), name='message'),
    path('unread-count', unreadCountView.as_view(), name='message'),




  
    
]