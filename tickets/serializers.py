from rest_framework import serializers
from .models import Client,Reservation,Film

class FlimSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = '__all__'

class ReservationSerialier(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'

class ClientSerialier(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['pk','reservation','nom', 'mobile']
