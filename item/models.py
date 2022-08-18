from django.db import models
from facilities.models import Facility
from items.models import *
import settings
# Create your models here.
class item(models.Model):
    facility=models.ForeignKey(Facility, on_delete=models.CASCADE, null=True)
    item_class=models.ForeignKey(ItemClass, on_delete=models.CASCADE, null=True)
    item_type=models.ForeignKey(ItemType, on_delete=models.CASCADE, null=True)
    code=models.CharField(max_length=20, null=True)
    TypeP=models.CharField(max_length=50, null=True)
    Manufacturer=models.CharField(max_length=50, null=True)
    Model=models.CharField(max_length=50, null=True)
    Type1=models.CharField(max_length=50, null=True)
    Type2=models.CharField(max_length=50, null=True)
    Type3=models.CharField(max_length=50, null=True)
    Type4=models.CharField(max_length=50, null=True)
    Type5=models.CharField(max_length=50, null=True)
    Type1P=models.CharField(max_length=50, null=True)
    #look at the items.json state to see the fields
    Height=models.IntegerField(null=True)
    Width=models.IntegerField(null=True)
    Length=models.IntegerField(null=True)
    GrossVolume=models.IntegerField(null=True)
    NetShippingVolume=models.IntegerField(null=True)
    Weightkg=models.IntegerField(null=True)
    ExternalSize=models.CharField(max_length=50, null=True)
    NumberOfDoors=models.IntegerField(null=True)
