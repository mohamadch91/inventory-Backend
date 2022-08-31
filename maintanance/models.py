from email.headerregistry import ParameterizedMIMEHeader
from importlib.metadata import requires
from django.db import models
from items.models import *
# Create your models here.
from item.models import item


class maintanance(models.Model):
    id=models.AutoField(primary_key=True)
    item_class=models.ForeignKey(ItemClass,models.CASCADE,null=True,blank=True)
    item_type=models.ForeignKey(ItemType,models.CASCADE,null=True,blank=True)
    code=models.CharField(max_length=20,blank=True,null=True)
    name=models.CharField(max_length=100,blank=True,null=True)
    enable=models.BooleanField(default=True,blank=True,null=True)
    freq=models.IntegerField(blank=True,null=True)
    requires=models.BooleanField(blank=True,null=True,default=True)
    freq_in_loc=models.IntegerField(blank=True,null=True)
    
class maintancegp(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50,blank=True,null=True)
    enable=models.BooleanField(default=True,blank=True,null=True)    
    item_class=models.ForeignKey(ItemClass,models.CASCADE,null=True,blank=True)
    item_type=models.ForeignKey(ItemType,models.CASCADE,null=True,blank=True)        
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class activeMaintance(models.Model):
    id=models.AutoField(primary_key=True)
    maintanance=models.ForeignKey(maintanance,models.DO_NOTHING,blank=True,null=True)
    maintanncegp=models.ForeignKey(maintancegp,models.DO_NOTHING,blank=True,null=True)
    enable=models.BooleanField(default=True,blank=True,null=True)            
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class toDoMaintance(models.Model):
    id=models.AutoField(primary_key=True)
    maintanance=models.ForeignKey(maintanance,models.DO_NOTHING,blank=True,null=True)
    maintanncegp=models.ForeignKey(maintancegp,models.DO_NOTHING,blank=True,null=True)
    item=models.ForeignKey(item,models.DO_NOTHING,blank=True,null=True)
    done=models.BooleanField(default=False,blank=True,null=True)            
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class doneMaintance(models.Model):
    id=models.AutoField(primary_key=True)
    maintanance=models.ForeignKey(maintanance,models.DO_NOTHING,blank=True,null=True)
    maintanncegp=models.ForeignKey(maintancegp,models.DO_NOTHING,blank=True,null=True)
    done=models.BooleanField(default=True,blank=True,null=True)     
    item=models.ForeignKey(item,models.DO_NOTHING,blank=True,null=True)       
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)