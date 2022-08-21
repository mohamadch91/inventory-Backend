from cgitb import enable
from faulthandler import disable
from pyexpat import model
from unicodedata import digit, name
from django.db import models
from items.models import ItemType
# Create your models here.

class relatedFacility(models.Model):
    class topics(models.TextChoices):
        gen = 'Facility general information'
        ser  = 'Information about services provided'
        phy='Facility physical conditions'
        HR = 'Human resource information'
        other ='Other optional fields'
        other1='Other'

    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=80)
    active=models.BooleanField(default=True)
    required=models.BooleanField(default=False)
    topic=models.CharField(max_length=50,choices=topics.choices,null=True,default=topics.gen)
    type=models.CharField(max_length=20)
    state=models.CharField(max_length=20,null=True)
    disabled=models.BooleanField(default=False)
 
class Field(models.Model):
    class topics(models.TextChoices):
        other = 'Type'
        Physical  = 'Physical fields'
        Condition='Condition fields'
        cold = 'Fields specific to cold chain equipment'
        Electrical ='Electrical fields'
        Financial='Financial fields'
        Different='Different codes'
        PQS='PQS/PIS fields'
        Dry='Dry store fields'
        Add='Other additional and optional fields'

    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=20)
    topic=models.CharField(max_length=50,choices=topics.choices)
    type=models.CharField(max_length=20)
    state=models.CharField(max_length=20,null=True)

class relatedItemType(models.Model):
    id=models.AutoField(primary_key=True)
    required=models.BooleanField(default=False)
    itemtype=models.ForeignKey(ItemType, on_delete=models.CASCADE)
    field=models.ForeignKey(Field, on_delete=models.CASCADE)

        
class facilityParam(models.Model):
    id=models.AutoField(primary_key=True)
    fieldid=models.ForeignKey(relatedFacility, on_delete=models.CASCADE)
    order=models.IntegerField(default=1)
    


class facilityParamDescription(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    order=models.IntegerField(default=1)
    enabled=models.BooleanField(default=True)
    paramid=models.ForeignKey(facilityParam, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class itemParam(models.Model):
    id=models.AutoField(primary_key=True)
    fieldid=models.ForeignKey(Field, on_delete=models.CASCADE)
    order=models.IntegerField(default=1)
    

     
class itemParamDescription(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    order=models.IntegerField(default=1)
    enabled=models.BooleanField(default=True)
    paramid=models.ForeignKey(itemParam, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Facilityvalidation:
    id=models.AutoField(primary_key=True)
    fieldid=models.ForeignKey(relatedFacility, on_delete=models.CASCADE)
    digits=models.IntegerField(default=0)
    min=models.IntegerField(default=0)
    max=models.IntegerField(default=0)
    float=models.BooleanField(default=False)
    floating=models.IntegerField(default=0)

class Itemvalidation:
    id=models.AutoField(primary_key=True)
    fieldid=models.ForeignKey(Field, on_delete=models.CASCADE)
    digits=models.IntegerField(default=0)
    min=models.IntegerField(default=0)
    max=models.IntegerField(default=0)
    float=models.BooleanField(default=False)
    floating=models.IntegerField(default=0)    