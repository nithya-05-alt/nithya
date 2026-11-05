from django.db import models
class employee(models.Model):
    name=models.CharField(max_length=1000)
    salary=models.IntegerField()
    department=models.CharField(max_length=1000)
    
# Create your models here.
