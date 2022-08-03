from django.db import models

# Create your models here.


class CountryConfig(models.Model):
    class TP(models.TextChoices):
        general = 'General population'
        under='Under-1 Population'
    country = models.CharField(max_length=50, blank=True, null=True)
    codecountry = models.CharField(db_column='CodeCountry', max_length=10, blank=True, null=True)  # Field name made lowercase.
    currency = models.CharField(db_column='Currency', max_length=50, blank=True, null=True)  # Field name made lowercase.
    levels = models.IntegerField(db_column='Levels', blank=True, null=True)  # Field name made lowercase.
    logo = models.ImageField(db_column='Logo', max_length=200, blank=True, null=True)  # Field name made lowercase.
    secondLogo = models.ImageField(db_column='SecondLogo', max_length=200, blank=True, null=True)  # Field name made lowercase.
    poptarget =models.CharField(db_column='PopTarget',max_length=20,choices=TP.choices, null=True)
    poprate = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    havehr = models.BooleanField(blank=True, null=True)
    mainlocation = models.CharField(max_length=100, blank=True, null=True)
    logo2 = models.CharField(db_column='Logo2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    usingtool = models.BooleanField(db_column='usingTool', blank=True, null=True)  # Field name made lowercase.
    usingmaintenance = models.BooleanField(db_column='usingMaintenance', blank=True, null=True)  # Field name made lowercase.
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'CountryConfig'

class LevelConfig(models.Model):
    country=models.ForeignKey(CountryConfig,on_delete=models.CASCADE,blank=True,null=True)
    maxpop = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    minpop = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    uppervol = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    undervol = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    maxpopu1 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    minpopu1 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    m25vol = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    m70vol = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    m25volnew = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    m70volnew = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    uppervolnew = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    undervolnew = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    dryvol = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    dryvolnew = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    parent=models.ForeignKey('self',on_delete=models.CASCADE,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'LevelConfig'