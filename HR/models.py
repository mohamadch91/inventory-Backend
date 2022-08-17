from django.db import models
from facilities.models import Facility
# Create your models here.

class HR (models.Model):
    id=models.AutoField(primary_key=True)
    facility=models.ForeignKey(Facility, on_delete=models.CASCADE)
    full_name=models.CharField(max_length=100,blank=True,null=True)
    position_level=models.CharField(max_length=100,blank=True,null=True)
    educatioin_level=models.CharField(max_length=100,blank=True,null=True)
    years_in_service=models.IntegerField(   blank=True,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    year_in_position=models.IntegerField(blank=True,null=True)