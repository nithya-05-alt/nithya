from django.db import models
class students(models.Model):
    name=models.CharField(max_length=1000)
    study=models.CharField(max_length=1000)
    phone=models.IntegerField()
#Create your models here.
