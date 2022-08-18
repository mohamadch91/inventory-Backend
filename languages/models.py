from pyexpat import model
from django.db import models

# Create your models here.

class languages(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100,blank=True,null=True)
    def __str__(self):
        return self.name

class languages_words(models.Model):
    id=models.AutoField(primary_key=True)
    language=models.ForeignKey(languages, on_delete=models.CASCADE, blank=True, null=True)
    word=models.CharField(max_length=100,blank=True,null=True)
    translate=models.CharField(max_length=100,blank=True,null=True)

    def __str__(self):
        return self.word

