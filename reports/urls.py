from django.urls import path
from .views import *



urlpatterns = [

      path('excel', exportExcel.as_view(), name='export excel'),
]