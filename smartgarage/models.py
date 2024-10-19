from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password) 
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    fullname = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['fullname']

    def __str__(self):
        return self.email


class Garage(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=35,unique=True,null=True)
    description = models.CharField(max_length=70)
    contact_num = models.IntegerField()
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

    def calculate_cost(self):
        time_difference = self.end_time - self.start_time
        return (time_difference.total_seconds() / 60) * self.garage_id.price
