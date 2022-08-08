from django.urls import path
from .views import *


urlpatterns = [
    path('', userDataView.as_view(), name='user-data'),
]