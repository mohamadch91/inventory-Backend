from faulthandler import disable
from pyexpat import model
from unicodedata import name
from django.db import models
from items.models import ItemType
# Create your models here.

class relatedFacility(models.Model):
    class topics(models.TextChoices):
        gen = 'Facility genera information'
        ser  = 'Information about services provided'
        phy='Facility physical conditions'
        HR = 'Human resource information'
        other ='Other optional fields'
        other1='Other'

    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=20)
    active=models.BooleanField(default=True)
    required=models.BooleanField(default=False)
    topic=models.CharField(max_length=50,choices=topics.choices,null=True,default=topics.gen)
    type=models.CharField(max_length=20)
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

class relatedItemType(models.Model):
    id=models.AutoField(primary_key=True)
    required=models.BooleanField(default=False)
    itemtype=models.ForeignKey(ItemType, on_delete=models.CASCADE)
    field=models.ForeignKey(Field, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
