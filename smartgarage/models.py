
from django.contrib.auth.models import AbstractBaseUser
from django.db import models


# Create your models here.
class User(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    mail = models.EmailField(unique=True)
    fullname = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255)

class Admin(models.Model):
    id = models.AutoField(primary_key=True)
    mail = models.EmailField(unique=True)
    fullname = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255)

class Garage(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=35,unique=True,null=True)
    description = models.CharField(max_length=70)
    contantnum = models.IntegerField()
    price = models.FloatField()
    longitude = models.FloatField()
    latitude = models.FloatField()
    totalslots = models.IntegerField()

class Reservation(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    garage_id = models.ForeignKey(Garage, on_delete=models.CASCADE)
    start_time=models.DateTimeField()
    end_time=models.DateTimeField(null=True, blank=True)
    reservation_cost=models.FloatField(null=True, blank=True)

