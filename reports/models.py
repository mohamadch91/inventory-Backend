from django.db import models

# Create your models here.
from facilities.models import Facility
from settings.models import LevelConfig
class gapSave(models.Model):
    id=models.AutoField(primary_key=True)
    facility=models.ForeignKey(Facility,on_delete=models.DO_NOTHING,related_name="facility_gap")
    parent_fac=models.ForeignKey(Facility,on_delete=models.DO_NOTHING,related_name="parent_fac")
    level=models.ForeignKey(LevelConfig,on_delete=models.DO_NOTHING,related_name="level")
    code=models.CharField(max_length=20)
    condition=models.CharField(max_length=100,default="")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    req_capacity=models.FloatField(default=0)
    available=models.FloatField(default=0)
    func_cap=models.FloatField(default=0)
    exces=models.FloatField(default=0)
    planned=models.BooleanField(default=False)
