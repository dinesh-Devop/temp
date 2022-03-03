from asyncio.windows_events import NULL
from django.db import models
from django.db.models.expressions import F
from django.db.models.fields import EmailField
from django_mysql.models import ListCharField
from django.contrib.auth.models import User
from django import forms



class txt(models.Model):
    file_name=models.FileField(verbose_name= '')
    activated =models.BooleanField(default=False)

class csv(models.Model):
    file_name=models.FileField(upload_to='csv',verbose_name= '')
    activated =models.BooleanField(default=False)
    


    

class Admins(models.Model):
    name   = models.CharField(blank=True, max_length=100,default="",null=True)
    title   = models.CharField(blank=True, max_length=100,default="",null=True)
    article  = models.CharField(blank=True, max_length=10000,default="",null=True)
    subject  = models.CharField(blank=True, max_length=10000,default="",null=True)
  
    photolink  = models.CharField(blank=True, max_length=10000,default="",null=True)

