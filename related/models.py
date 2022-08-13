from faulthandler import disable
from pyexpat import model
from unicodedata import name
from django.db import models
from items.models import ItemType
# Create your models here.

class relatedFacility(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=20)
    active=models.BooleanField(default=True)
    required=models.BooleanField(default=False)
    type=models.CharField(max_length=20)
    disabled=models.BooleanField(default=False)
 
class Field(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=20)
    type=models.CharField(max_length=20)

class relatedItemType(models.Model):
    id=models.AutoField(primary_key=True)
    active=models.BooleanField(default=True)
    required=models.BooleanField(default=False)
    disabled=models.BooleanField(default=False)
    itemtype=models.ForeignKey(ItemType, on_delete=models.CASCADE)
    field=models.ForeignKey(Field, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
