from django.db import models

from otpauth.models import User, Corporation


class ImageGallery(models.Model):
    created = models.DateTimeField(auto_now_add=True)


class Image(models.Model):
    gallery = models.ForeignKey(ImageGallery, on_delete=models.CASCADE)
    image = models.ImageField()


class CorporateModel:
    corporation = models.ForeignKey(Corporation, on_delete=models.CASCADE)


class HasLocation:
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)


class Hotel(CorporateModel, HasLocation, models.Model):
    name = models.TextField()
    description = models.TextField()
    gallery = models.ForeignKey(ImageGallery, on_delete=models.CASCADE, null=True, blank=True)


class HotelRoom(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    available = models.BooleanField(default=False)
    beds = models.IntegerField()
    price = models.IntegerField()
    description = models.TextField()


class RentingCenter(CorporateModel, HasLocation, models.Model):
    name = models.TextField()
    description = models.TextField()
    gallery = models.ForeignKey(ImageGallery, on_delete=models.CASCADE, null=True, blank=True)


class Rental(models.Model):
    center = models.ForeignKey(RentingCenter, on_delete=models.CASCADE)
    available = models.BooleanField(default=False)
    name = models.TextField()
    description = models.TextField()
    gallery = models.ForeignKey(ImageGallery, on_delete=models.CASCADE, null=True, blank=True)
    price = models.IntegerField()


class MedicalFacility(CorporateModel, HasLocation, models.Model):
    name = models.TextField()
    description = models.TextField()
    gallery = models.ForeignKey(ImageGallery, on_delete=models.CASCADE, null=True, blank=True)


class MedicalService(models.Model):
    facility = models.ForeignKey(MedicalFacility, on_delete=models.CASCADE)
    available = models.BooleanField(default=False)
    name = models.TextField()
    description = models.TextField()
    gallery = models.ForeignKey(ImageGallery, on_delete=models.CASCADE, null=True, blank=True)


class Trip(CorporateModel, models.Model):
    available = models.BooleanField(default=False)
    available_until = models.DateTimeField()
    name = models.TextField()
    description = models.TextField()
    gallery = models.ForeignKey(ImageGallery, on_delete=models.CASCADE, null=True, blank=True)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, null=True, blank=True)
    renting_center = models.ForeignKey(RentingCenter, on_delete=models.CASCADE, null=True, blank=True)
    medical_facility = models.ForeignKey(MedicalFacility, on_delete=models.CASCADE, null=True, blank=True)


class Activity(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    name = models.TextField()
    description = models.TextField()
    gallery = models.ForeignKey(ImageGallery, on_delete=models.CASCADE, null=True, blank=True)


class Order(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    orderer = models.ForeignKey(User, related_name='orderer', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    ordered_room = models.ForeignKey(HotelRoom, on_delete=models.CASCADE, null=True, blank=True)
    ordered_rental = models.ForeignKey(Rental, on_delete=models.CASCADE, null=True, blank=True)
    ordered_medical_service = models.ForeignKey(MedicalService, on_delete=models.CASCADE, null=True, blank=True)
    notes = models.TextField()
    operator = models.ForeignKey(User, related_name='operator', on_delete=models.CASCADE)
    approved = models.BooleanField(default=False)
    operator_message = models.TextField()


class OrderedActivity(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
