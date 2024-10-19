from django.contrib import admin
from .models import User,Garage,Reservation
# Register your models here.
admin.site.register(User)
admin.site.register(Garage)
admin.site.register(Reservation)