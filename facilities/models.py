import django
from django.db import models
from settings.models import CountryConfig, LevelConfig
from django.conf import settings
# Create your models here.

class Facility(models.Model):
    country=models.ForeignKey(CountryConfig, on_delete=models.CASCADE,blank=True,null=True)
    parentid = models.ForeignKey('self',on_delete=models.CASCADE,blank=True,null=True) # Field name made lowercase.
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    code = models.CharField(max_length=50, blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    level = models.ForeignKey(LevelConfig, on_delete=models.CASCADE, blank=True, null=True)
    populationnumber = models.IntegerField(db_column='populationNumber', blank=True, null=True)  # Field name made lowercase.
    childrennumber = models.IntegerField(db_column='childrenNumber', blank=True, null=True)  # Field name made lowercase.
    year = models.IntegerField(blank=True, null=True)
    completerstaffname = models.ForeignKey(settings.AUTH_USER_MODEL,db_column='completerStaff',on_delete=models.CASCADE, max_length=50, blank=True, null=True)  # Field name made lowercase.
    coverage = models.IntegerField(db_column='Coverage', blank=True, null=True)  # Field name made lowercase.
    coverage1 = models.IntegerField(db_column='Coverage1', blank=True, null=True)  # Field name made lowercase.
    province = models.CharField(max_length=50,db_column='province', blank=True, null=True)  # Field name made lowercase.
    district = models.CharField(max_length=50, blank=True, null=True)

    zone = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
   
    address = models.CharField(max_length=200, blank=True, null=True)
    postalcode = models.CharField(db_column='postalCode', max_length=12, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(max_length=100, blank=True, null=True)
    gpsCordinate = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    haveinternet = models.BooleanField(db_column='haveInternet', blank=True, null=True)  # Field name made lowercase.
    ownership = models.CharField(max_length=50, blank=True, null=True)
    roadtype = models.CharField(db_column='roadType', max_length=50,blank=True, null=True)  # Field name made lowercase.
    climate = models.IntegerField(blank=True, null=True)
    distancefromparent = models.IntegerField(db_column='distanceFromParent', blank=True, null=True)  # Field name made lowercase.
    timetoparent = models.CharField(db_column='timeToParent', max_length=50, blank=True, null=True)  # Field name made lowercase.
    receivingvaccmode = models.IntegerField(db_column='receivingVaccMode', blank=True, null=True)  # Field name made lowercase.
    haveimmservice = models.BooleanField(db_column='HaveImmService', blank=True, null=True)  # Field name made lowercase.
    typeimmservice = models.IntegerField(db_column='TypeImmService', blank=True, null=True)  # Field name made lowercase.
    numimmperweek = models.IntegerField(db_column='NumImmperWeek', blank=True, null=True)  # Field name made lowercase.
    havecovid19service = models.BooleanField(db_column='HaveCovid19Service', blank=True, null=True)  # Field name made lowercase.
    countvacc1 = models.IntegerField(db_column='countVacc1', blank=True, null=True)  # Field name made lowercase.
    countvacc2 = models.IntegerField(db_column='countVacc2', blank=True, null=True)  # Field name made lowercase.
    other1 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    other2 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    other3 = models.BooleanField(blank=True, null=True)
    other4 = models.BooleanField(blank=True, null=True)
    other5 = models.CharField(max_length=100, blank=True, null=True)
    other6 = models.CharField(max_length=100, blank=True, null=True)
    transportmode = models.IntegerField(db_column='transportMode', blank=True, null=True)  # Field name made lowercase.
    startwork = models.CharField(db_column='startWork', max_length=50, blank=True, null=True)  # Field name made lowercase.
    endwork = models.CharField(db_column='endWork', max_length=50, blank=True, null=True)  # Field name made lowercase.
    staffnumber = models.IntegerField(db_column='staffNumber', blank=True, null=True)  # Field name made lowercase.
    numprofstaff = models.IntegerField(db_column='NumProfStaff', blank=True, null=True)  # Field name made lowercase.
    numvaccstaff = models.IntegerField(db_column='NumVaccStaff', blank=True, null=True)  # Field name made lowercase.
    numdriverstaff = models.IntegerField(db_column='NumDriverStaff', blank=True, null=True)  # Field name made lowercase.
    powersource = models.IntegerField(db_column='powerSource', blank=True, null=True)  # Field name made lowercase.
    havegenerator = models.BooleanField(db_column='HaveGenerator', blank=True, null=True)  # Field name made lowercase.
    barcode = models.CharField(max_length=100, blank=True, null=True)
    functionstatus = models.IntegerField(blank=True, null=True)
    remark = models.CharField(max_length=500, blank=True, null=True)
    completerstaffsign = models.CharField(db_column='completerStaffSign', max_length=50, blank=True, null=True)  # Field name made lowercase.


    class Meta:
        db_table = 'Facility'
