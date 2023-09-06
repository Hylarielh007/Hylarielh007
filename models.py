from enum import unique
from django.db import models


class Coupon(models.Model):
    serial_number = models.CharField(max_length=50, unique=True)
    fuel_type = models.CharField(max_length=50)
    litres = models.CharField(max_length=50)
    receiving_date = models.DateField()
    
    def __str__(self):
        return self.serial_number
    
    
class Vehicle(models.Model):
    registration_number = models.CharField(max_length=50, unique=True)
    engine_capacity = models.CharField(max_length=50)
    distance_travelled = models.FloatField()
    
    def __str__(self):
        return self.registration_number
    

class Employee(models.Model):
    ec_number = models.CharField(unique=True, max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    
    def __str__(self):
        return self.ec_number
    
    
class Location(models.Model):
    ec_number = models.CharField(max_length=50)
    
    def __str__(self):
        return self.ec_number
    
    