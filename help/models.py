from django.db import models


# Create your models here.
class Help(models.Model):
    class choices(models.TextChoices):
        admin= 'admin'
        index= 'index'
        Facility_info= 'Facility_info'
        Facility_type= 'Facility_type'
        #do same for item and user
        Item_type= 'Item_type'
        User_type= 'User_type'
        #do same for item and user
        Item_info= 'Item_info'
        User_info= 'User_info'
        admin_guide= 'admin_guide'
    class language(models.TextChoices):
        #arabic english persian french russian
        arabic= 'arabic'
        english= 'english'
        persian= 'persian'
        french= 'french'
        russian= 'russian'

    page = models.CharField(max_length=20, choices=choices.choices ,blank=True, null=True)
    lang = models.CharField(max_length=20, choices=language.choices ,blank=True, null=True)
    abr = models.FileField(upload_to="help",null=True)
