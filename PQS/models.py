from django.db import models

# Create your models here.
class pqs4(models.Model):
    id=models.AutoField(primary_key=True)

    pqsnumber = models.CharField(db_column='PQSNumber', max_length=100)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=100, blank=True, null=True)  # Field name made lowercase.
    manufacturer = models.CharField(db_column='Manufacturer', max_length=100, blank=True, null=True)  # Field name made lowercase.
    model = models.CharField(db_column='Model', max_length=100, blank=True, null=True)  # Field name made lowercase.
    vaccinenetstoragecapacity = models.FloatField(db_column='VaccineNetStorageCapacity', blank=True, null=True)  # Field name made lowercase.
    coolantpacknominalcapacity = models.FloatField(db_column='CoolantPackNominalCapacity', blank=True, null=True)  # Field name made lowercase.
    numbercoolantpacks = models.IntegerField(db_column='NumberCoolantPacks', blank=True, null=True)  # Field name made lowercase.
    externalvolume = models.FloatField(db_column='ExternalVolume', blank=True, null=True)  # Field name made lowercase.


class pqs3(models.Model):
    id=models.AutoField(primary_key=True)
    description = models.CharField(db_column='Description', max_length=100, blank=True, null=True)  # Field name made lowercase.
    make = models.CharField(db_column='Make', max_length=100, blank=True, null=True)  # Field name made lowercase.
    model = models.CharField(db_column='Model', max_length=100, blank=True, null=True)  # Field name made lowercase.
    pqscode = models.CharField(db_column='PQScode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    refrigerant = models.CharField(db_column='Refrigerant', max_length=50, blank=True, null=True)  # Field name made lowercase.
    refrigeratorcapacity = models.FloatField(db_column='RefrigeratorCapacity', blank=True, null=True)  # Field name made lowercase.
    freezercapacity = models.FloatField(db_column='FreezerCapacity', blank=True, null=True)  # Field name made lowercase.
    kg_24_hrs = models.FloatField(blank=True, null=True)
    h = models.FloatField(db_column='H', blank=True, null=True)  # Field name made lowercase.
    w = models.FloatField(db_column='W', blank=True, null=True)  # Field name made lowercase.
    l = models.FloatField(db_column='L', blank=True, null=True)  # Field name made lowercase.
