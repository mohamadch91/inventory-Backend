from django.db import models

from django.contrib.auth.models import AbstractUser
from facilities.models import Facility



class User(AbstractUser):
  
    name = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    idnumber = models.CharField(max_length=50, blank=True, null=True)
    position = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    facadmin = models.BooleanField(blank=True, null=True)
    itemadmin = models.BooleanField(blank=True, null=True)
    reportadmin = models.BooleanField(blank=True, null=True)
    useradmin = models.BooleanField(blank=True, null=True)
    facilityid=models.ForeignKey(Facility, on_delete=models.CASCADE, blank=True, null=True)

    # USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    class Meta:
        # managed = False
        db_table = 'User'
 
 