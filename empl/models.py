from django.db import models
from datetime import timezone

# Create your models here.


class Location(models.Model):
    place = models.CharField(max_length=200,unique=True,null=True)

    def __str__(self):
        return self.place
    

class VehicleClass(models.Model):
    vclass= models.CharField(max_length=200,unique=True,null=True)

    def __str__(self):
        return self.vclass
    


class Vehicle(models.Model):
    vehicle_no = models.CharField(max_length=200,null=True,unique=True)
    owner = models.CharField(max_length=200,null=True)
    model = models.CharField(max_length=200,null=True)
    vehicle_class = models.ManyToManyField(VehicleClass)
    chassis_no = models.CharField(max_length=200,null=True)
    reg_date = models.DateField(null=True,auto_now=timezone)
    insurance_valid_upto = models.DateField(null=True)
    tax_valid =models.DateField(null=True)
    fitness_valid = models.DateField(null=True)
    permit_valid = models.DateField(null=True)
    pollution_control_valid = models.DateField(null=True)
    location = models.ManyToManyField(Location)

    def __str__(self):
        return self.vehicle_no
    
class Driver(models.Model):
    name = models.CharField(max_length=200,null=True)
    address = models.CharField(max_length=200,null=True)
    phone_no = models.IntegerField(null=True)
    bio = models.TextField(blank=True)
    vehicle = models.ManyToManyField(Vehicle)
    def __str__(self):
        return self.name
    

class Diesel(models.Model):
    # driver = models.ManyToManyField(Driver,related_name='driv')
    vehicle= models.ManyToManyField(Vehicle,related_name='diesels')
    price = models.IntegerField(null=True)
    date = models.DateField(null=True)
    
    def __str__(self):
       return f'{self.date}'
   
    


class Maintenance(models.Model):
    vehicle = models.ManyToManyField(Vehicle,related_name='maintenancevehicle')
    price = models.IntegerField(null=True)
    date = models.DateField(null=True)
    service_type = models.CharField(max_length=200,null=True)
    location = models.ManyToManyField(Location)

    def __str__(self):
        return self.service_type
    

class SpareParts(models.Model):
    date = models.DateField(null=True)

    vehicle = models.ManyToManyField(Vehicle,related_name='spareparts')
    price = models.IntegerField(null=True)
    spare_id= models.CharField(max_length=200,null=True)
    quantity = models.IntegerField(null=True)

    def __str__(self):
        return self.spare_id
    



    


