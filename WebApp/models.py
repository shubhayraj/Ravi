from django.db import models

# Create your models here.
class Employee(models.Model):
    Empid=models.IntegerField()
    Empname=models.CharField(max_length=100)
    Desig=models.CharField(max_length=100)
    Emppic=models.FileField()
    Empsal=models.IntegerField()
    Dob=models.DateField()
    Joind=models.DateField()
    
