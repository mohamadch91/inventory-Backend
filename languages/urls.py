from django.urls import path
from .views import *


urlpatterns = [

    path('', languageView.as_view(), name='language'),
    path('translation', getlanguages.as_view(), name='languages'),


  
    
]