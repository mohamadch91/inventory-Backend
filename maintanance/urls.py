from django.urls import path
from .views import *


urlpatterns = [

    path('', itemclassView.as_view(), name='Itemclass'),
    path('helper', itemtypeView.as_view(), name='Itemtype'),
    path('group', itemtypeByclass.as_view(), name='Itembyclass'),
    path('itemTinLevels', itemTypeinLevels.as_view(), name='ItemtypeInLevels'),
    path('manufacturer', manufacturerView.as_view(), name='Manufacturer'),
    path('class-helper',manhelper.as_view(),name="helper")
    
]