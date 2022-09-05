from django.db import models


# Create your models here.
class Help(models.Model) :
    class choices(models.TextChoices):
            dashboard = "Dashboard"  
            facilities = "Facilities"  
            hr = "Human Resources"  
            user = "User"  
            message = "Message"  
            reports = "Reports"  
            settings = "Settings"  
            about_iga = "About-IGA"  
    class language(models.TextChoices):
        #arabic english persian french russian
        en = "English"  
        fr = "Français"  
        ar = "العربية"  
        fa = "فارسی"  
        es = "Español"  
        ru = "Русский"  

    page = models.CharField(max_length=20 , choices=choices.choices , blank=True , null=True)
    lang = models.CharField(max_length=20  ,choices=language.choices , blank=True , null=True)
    abr = models.FileField(upload_to="help" ,null=True,blank=True)
