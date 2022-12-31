from django.db import models


# Create your models here.
class Help(models.Model) :
    class choices(models.TextChoices):
            dashboard = "dashboard"  
            facilities = "facilities"  
            hr = "hr"  
            user = "user"  
            message = "message"  
            reports = "reports"  
            settings = "settings"  
            about_iga = "about-iga"  
    class language(models.TextChoices):
        #arabic english persian french russian
        en = "en"  
        fr = "fr"  
        ar = "ar"  
        ot = "ot"  
        es = "es"  
        ru = "ru"  
        uk ="uk"
        vi ="vi"

    page = models.CharField(max_length=20 , choices=choices.choices , blank=True , null=True)
    lang = models.CharField(max_length=20  ,choices=language.choices , blank=True , null=True)
    abr = models.FileField(upload_to="help" ,null=True,blank=True)

    def __str__(self):
        return self.page +"--" +self.lang + "--"+str(self.abr)
