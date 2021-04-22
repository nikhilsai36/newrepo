from django.db import models

# Create your models here.
class Vehicle(models.Model):
    car_name = models.CharField(max_length=15, null=True)
    car_color = models.CharField(max_length=10, null=True)
    car_regNo = models.CharField(max_length=12, null=True)
    car_chassisno = models.TextField(max_length=15)
    car_manfacturing_year = models.DateField()
