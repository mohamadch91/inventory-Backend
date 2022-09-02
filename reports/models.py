from django.db import models

# Create your models here.
from facilities.models import Facility
from settings.models import LevelConfig
class gapSave(models.Model):
    id=models.AutoField(primary_key=True)
    facility=models.ForeignKey(Facility,on_delete=models.DO_NOTHING,related_name="facility_gap",null=True)
    parent_fac=models.ForeignKey(Facility,on_delete=models.DO_NOTHING,related_name="parent_fac",null=True,blank=True)
    level=models.ForeignKey(LevelConfig,on_delete=models.DO_NOTHING,related_name="level",null=True,blank=True)
    code=models.CharField(max_length=20,blank=True,null=True)
    condition=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    req_capacity=models.FloatField(default=0)
    available=models.FloatField(default=0)
    func_cap=models.FloatField(default=0)
    exces=models.FloatField(default=0)
    calculate_for=models.CharField(max_length=20,blank=True,null=True)
    general=models.IntegerField(default=0)
    under_1=models.IntegerField(default=0)
    planned=models.BooleanField(default=False)

class plannedGap(models.Model):
    id=models.AutoField(primary_key=True)
    gap=models.ForeignKey(Facility,on_delete=models.DO_NOTHING,related_name="saved_gap",null=True)
    pqs_type=models.IntegerField()
    pqs_id=models.IntegerField()
    provided=models.BooleanField(default=False)
    asiign=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)



    