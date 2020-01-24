from rest_framework import serializers

from app import models


class ImageGallery(serializers.ModelSerializer):
    class Meta:
        model = models.ImageGallery
        fields = '__all__'


class Image(serializers.ModelSerializer):
    class Meta:
        model = models.Image
        fields = '__all__'


class Hotel(serializers.ModelSerializer):
    class Meta:
        model = models.Hotel
        fields = '__all__'


class HotelRoom(serializers.ModelSerializer):
    class Meta:
        model = models.HotelRoom
        fields = '__all__'


class RentingCenter(serializers.ModelSerializer):
    class Meta:
        model = models.RentingCenter
        fields = '__all__'


class Rental(serializers.ModelSerializer):
    class Meta:
        model = models.Rental
        fields = '__all__'


class MedicalFacility(serializers.ModelSerializer):
    class Meta:
        model = models.MedicalFacility
        fields = '__all__'


class MedicalService(serializers.ModelSerializer):
    class Meta:
        model = models.MedicalService
        fields = '__all__'


class Trip(serializers.ModelSerializer):
    class Meta:
        model = models.Trip
        fields = '__all__'


class Activity(serializers.ModelSerializer):
    class Meta:
        model = models.Activity
        fields = '__all__'


class Order(serializers.ModelSerializer):
    class Meta:
        model = models.Order
        fields = '__all__'


class OrderedActivity(serializers.ModelSerializer):
    class Meta:
        model = models.OrderedActivity
        fields = '__all__'
