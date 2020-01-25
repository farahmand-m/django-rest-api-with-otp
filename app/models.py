from django.db import models

from otpauth.models import User, Corporation


class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField()


class ImageGallery(models.Model):
    created = models.DateTimeField(auto_now_add=True)


class Image(models.Model):
    gallery = models.ForeignKey(ImageGallery, on_delete=models.CASCADE)
    image = models.ImageField()


class ServiceCenter(models.Model):
    corporation = models.ForeignKey(Corporation, on_delete=models.CASCADE)
    name = models.TextField()
    description = models.TextField()
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    gallery = models.ForeignKey(ImageGallery, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        abstract = True


class Hotel(ServiceCenter):
    class Meta:
        verbose_name = 'Hotel'
        verbose_name_plural = 'Hotels'


class RentingCenter(ServiceCenter):
    class Meta:
        verbose_name = 'Renting Center'
        verbose_name_plural = 'Renting Centers'


class MedicalFacility(ServiceCenter):
    class Meta:
        verbose_name = 'Medical Facility'
        verbose_name_plural = 'Medical Facilities'


class Service(models.Model):
    available = models.BooleanField(default=False)
    description = models.TextField()
    gallery = models.ForeignKey(ImageGallery, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        abstract = True


class HotelRoom(Service):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    beds = models.IntegerField()
    price = models.IntegerField()


class Rental(Service):
    center = models.ForeignKey(RentingCenter, on_delete=models.CASCADE)
    name = models.TextField()
    price = models.IntegerField()


class MedicalService(Service):
    facility = models.ForeignKey(MedicalFacility, on_delete=models.CASCADE)
    name = models.TextField()


class Trip(models.Model):
    available = models.BooleanField(default=False)
    available_until = models.DateTimeField()
    name = models.TextField()
    description = models.TextField()
    gallery = models.ForeignKey(ImageGallery, on_delete=models.CASCADE, null=True, blank=True)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, null=True, blank=True)
    renting_center = models.ForeignKey(RentingCenter, on_delete=models.CASCADE, null=True, blank=True)
    medical_facility = models.ForeignKey(MedicalFacility, on_delete=models.CASCADE, null=True, blank=True)


class Activity(Service):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    name = models.TextField()


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
