from lib2to3.pgen2 import driver
from pyexpat import native_encoding
import django
from django.db import models
from django.conf import settings
from settings.models import CountryConfig, LevelConfig

# Create your models here.

class Facility(models.Model):
    id=models.AutoField(primary_key=True)
    country=models.ForeignKey(CountryConfig, on_delete=models.DO_NOTHING,blank=True,null=True)
    parentid = models.ForeignKey('self',on_delete=models.DO_NOTHING,blank=True,null=True) # Field name made lowercase.
    level = models.ForeignKey(LevelConfig, on_delete=models.DO_NOTHING, blank=True, null=True)
    name=models.CharField(max_length=100,blank=True,null=True)
    code=models.CharField(  max_length=50,blank=True,null=True)
    type = models.CharField(null=True, blank=True, max_length=100)
    populationnumber = models.IntegerField(db_column='populationNumber', blank=True, null=True)  # Field name made lowercase.
    childrennumber = models.IntegerField(db_column='childrenNumber', blank=True, null=True)  # Field name made lowercase.
    loverlevelfac=models.IntegerField(db_column='loverLevelFac', blank=True, null=True)  # Field name made lowercase.
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    completerstaffname = models.ForeignKey(settings.AUTH_USER_MODEL,db_column='completerStaff',on_delete=models.CASCADE, max_length=50, blank=True, null=True)  # Field name made lowercase.
    province = models.CharField(max_length=50,db_column='province', blank=True, null=True)  # Field name made lowercase.
    zone = models.CharField(max_length=100, blank=True, null=True)
    district = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    postalcode = models.CharField(db_column='postalCode', max_length=12, blank=True, null=True)  # Field name made lowercase.
    national_code=models.CharField(max_length=20,blank=True,null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    gpsCordinate = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    land_phone = models.BooleanField(default=False)
    haveinternet = models.BooleanField(db_column='haveInternet', blank=True, null=True)  # Field name made lowercase.
    year = models.IntegerField(blank=True, null=True)
    is_functioning=models.BooleanField(default=True)
    climate=models.CharField(max_length=50,blank=True,null=True)
    ownership = models.CharField(max_length=50, blank=True, null=True)
    roadtype = models.CharField(db_column='roadType', max_length=50,blank=True, null=True)  # Field name made lowercase.
    distancefromparent = models.IntegerField(db_column='distanceFromParent', blank=True, null=True)  # Field name made lowercase.
    timetoparent = models.CharField(db_column='timeToParent', max_length=50, blank=True, null=True)  # Field name made lowercase.
    days_open =models.IntegerField(db_column='daysOpen', blank=True, null=True)  # Field name made lowercase.
    working_from=models.CharField(max_length=50,db_column='workingFrom', blank=True, null=True)  # Field name made lowercase.
    working_to=models.CharField(max_length=50,db_column='workingTo', blank=True, null=True)  # Field name made lowercase.
    recieve_mode=models.CharField(max_length=50,blank=True,null=True)
    transport_mode=models.CharField(max_length=50,blank=True,null=True)
    haveimmservice = models.BooleanField(db_column='HaveImmService', blank=True, null=True)  # Field name made lowercase.
    typeimmservice = models.IntegerField(db_column='TypeImmService', blank=True, null=True)  # Field name made lowercase.
    numimmperweek = models.IntegerField(db_column='NumImmperWeek', blank=True, null=True)  # Field name made lowercase.
    havecovid19service = models.BooleanField(db_column='HaveCovid19Service', blank=True, null=True)  # Field name made lowercase.
    coverageX1=models.IntegerField(db_column='CoverageX1', blank=True, null=True)  # Field name made lowercase.
    coverageX2=models.IntegerField(db_column='CoverageX2', blank=True, null=True)  # Field name made lowercase.
    #need x3
    coverageX3=models.IntegerField(db_column='CoverageX3', blank=True, null=True)  # Field name made lowercase.    
    coverageX4=models.IntegerField(db_column='CoverageX4', blank=True, null=True)  # Field name made lowercase.
    individualsX1=models.IntegerField(db_column='IndividualsX1', blank=True, null=True)  # Field name made lowercase.
    individualsX2=models.IntegerField(db_column='IndividualsX2', blank=True, null=True)  # Field name made lowercase.
    individualsX3=models.IntegerField(db_column='IndividualsX3', blank=True, null=True)  # Field name made lowercase.
    individualsX4=models.IntegerField(db_column='IndividualsX4', blank=True, null=True)  # Field name made lowercase.
    number_icepack=models.IntegerField(db_column='NumberIcepack', blank=True, null=True)  # Field name made lowercase.
    other_service=models.BooleanField(db_column='OtherService', blank=True, null=True)  # Field name made lowercase.
    other_services=models.CharField(max_length=50,blank=True,null=True)
    is_suitable=models.BooleanField(db_column='IsSuitable', blank=True, null=True)  # Field name made lowercase.
    
    is_suitable_reason=models.CharField(db_column='IsSuitableReason', max_length=50, blank=True, null=True)  # Field name made lowercase.
    havegen=models.BooleanField(db_column='HaveGen', blank=True, null=True)  # Field name made lowercase.
    powersource=models.CharField(db_column='PowerSource', max_length=50, blank=True, null=True)  # Field name made lowercase.
    maintance=models.CharField(db_column='Maintance', max_length=50, blank=True, null=True)  # Field name made lowercase.
    vac_num=models.IntegerField(db_column='VacNum', blank=True, null=True)  # Field name made lowercase.
    total_staff=models.IntegerField(db_column='TotalStaff', blank=True, null=True)  # Field name made lowercase.
    prof_staff=models.IntegerField(db_column='ProfStaff', blank=True, null=True)  # Field name made lowercase.
    nurses=models.IntegerField(db_column='Nurses', blank=True, null=True)  # Field name made lowercase.
    drivers=models.IntegerField(db_column='Drivers', blank=True, null=True)  # Field name made lowercase.
    other_staff=models.IntegerField(db_column='OtherStaff', blank=True, null=True)  # Field name made lowercase.
    other1 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    other2 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    other3 = models.BooleanField(blank=True, null=True)
    other4 = models.BooleanField(blank=True, null=True)
    other5 = models.CharField(max_length=100, blank=True, null=True)
    other6 = models.CharField(max_length=100, blank=True, null=True)
    remark = models.CharField(max_length=500, blank=True, null=True)
    completerstaffsign = models.CharField(db_column='completerStaffSign', max_length=50, blank=True, null=True)  # Field name made lowercase.
    is_deleted = models.BooleanField(db_column='isDeleted',default=False)  # Field name made lowercase.
    delete_reason=models.CharField(max_length=50,blank=True,null=True)
    other_code=models.CharField(max_length=50,blank=True,null=True)


    class Meta:
        db_table = 'Facility'

    def __str__(self) -> str:
        return self.name