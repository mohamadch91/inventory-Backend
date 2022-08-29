from django.urls import path
from .views import *



urlpatterns = [

      path('excel', exportExcel.as_view(), name='export excel'),
      path('facseg', facilitysegView.as_view(), name='facility segmentation'),
      path('subfacpop', subfacView.as_view(), name='Sub Facility population data'),


]