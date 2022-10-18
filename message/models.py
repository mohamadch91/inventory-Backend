from django.db import models
from facilities.models import Facility
# Create your models here.
from authen.models import User
# message model need sender reciever subject and body

class message(models.Model):
    id=models.AutoField(primary_key=True)
    sender=models.ForeignKey(Facility, on_delete=models.CASCADE, blank=True, null=True,related_name='sender')
    reciever=models.ForeignKey(Facility, on_delete=models.CASCADE, blank=True, null=True,related_name='reciever')
    subject=models.CharField(max_length=100,blank=True,null=True)
    body=models.TextField(max_length=500,blank=True,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    read=models.BooleanField(default=False)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.subject
class readedMessage(models.Model):
    id=models.AutoField(primary_key=True)
    message=models.ForeignKey(message, on_delete=models.CASCADE, blank=True, null=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.message.subject