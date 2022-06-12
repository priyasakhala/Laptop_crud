from django.db import models

# Create your models here.
class Laptop(models.Model):
    laptop_id = models.IntegerField()
    name = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    ram = models.CharField(max_length=50)
    rom = models.CharField(max_length=50)
    hdd = models.CharField(max_length=50)
    ssd = models.CharField(max_length=50)
    price = models.FloatField()