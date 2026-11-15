from django.db import models

# Create your models here.
class Employee(models.Model):

    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    salary = models.DecimalField(max_digits=10,decimal_places=2)
    department = models.CharField(max_length=200)
    location = models.CharField(max_length=200)