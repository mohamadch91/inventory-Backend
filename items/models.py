from pyexpat import model
from django.db import models
from settings.models import *
# Create your models here.

class ItemClass(models.Model):
    id=models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ItemType(models.Model):
    id=models.AutoField(primary_key=True)
    itemclass=models.ForeignKey(ItemClass, on_delete=models.CASCADE)
    title = models.CharField(max_length=100,unique=True)
    code = models.CharField(max_length=20, unique=True)
    active = models.BooleanField(default=True)
    havePQS=models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

class Itemtypelevel(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    itemtypeid = models.ForeignKey(ItemType,db_column='itemTypeID', blank=True, null=True, on_delete=models.CASCADE)  # Field name made lowercase.
    active=models.BooleanField(default=True)
    level = models.ForeignKey(LevelConfig,blank=True, null=True, on_delete=models.CASCADE)
   
