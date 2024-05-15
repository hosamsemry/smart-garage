from rest_framework import serializers
from .models import User,Garage,Admin,Reservation



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'mail', 'fullname', 'password']
        extra_kwargs = {'password': {'write_only': True}}  # To make the password field write-only


class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = ['id', 'mail', 'fullname', 'password']
        extra_kwargs = {'password': {'write_only': True}}  # To make the password field write-only

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'
class GarageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Garage
        fields = '__all__'
class StartReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ['id','user_id','garage_id','start_time']
class EndReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ['id','end_time','reservation_cost']