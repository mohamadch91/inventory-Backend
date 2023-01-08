from django.urls import path
from .views import *


urlpatterns = [
    path('related-facility/', relatedfacilityView.as_view(), name='related facility view'),
    path('item-fields', fieldView.as_view(), name='item fields view'),
    path('related-item-type', relatedItemTypeView.as_view(), name='related item type view'),
    path('params/', paramView.as_view(), name='params view'),
    path('db/', dbView.as_view(), name='db view'),
    path('excel/', Excelconvert.as_view(), name='db view'),
    
    
    
]