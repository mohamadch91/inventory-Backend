from django.urls import path
from .views import *


urlpatterns = [

    path('itemClass', itemclassView.as_view(), name='Itemclass'),
    path('itemType', itemtypeView.as_view(), name='Itemtype'),
    path('itembyclass', itemtypeByclass.as_view(), name='Itembyclass'),
    path('itemTinLevels', itemTypeinLevels.as_view(), name='ItemtypeInLevels'),
    path('manufacturer', manufacturerView.as_view(), name='Manufacturer'),
    path('class-helper',manhelper.as_view(),name="helper"),
    path('db',itemdb.as_view(),name="helper")
    

    
]