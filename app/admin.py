from django.contrib import admin

from app import models


class ImageInlineModel(admin.StackedInline):
    model = models.Image


class ImageGalleryAdminModel(admin.ModelAdmin):
    inlines = [ImageInlineModel]


class HotelRoomInlineModel(admin.StackedInline):
    model = models.HotelRoom


class HotelAdminModel(admin.ModelAdmin):
    inlines = [HotelRoomInlineModel]


class RentalInlineModel(admin.StackedInline):
    model = models.Rental


class RentingCenterAdminModel(admin.ModelAdmin):
    inlines = [RentalInlineModel]


class MedicalServiceInlineModel(admin.StackedInline):
    model = models.MedicalService


class MedicalFacilityAdminModel(admin.ModelAdmin):
    inlines = [MedicalServiceInlineModel]


class ActivityInlineModel(admin.StackedInline):
    model = models.Activity


class TripAdminModel(admin.ModelAdmin):
    inlines = [ActivityInlineModel]


class OrderedActivityInlineModel(admin.StackedInline):
    model = models.OrderedActivity


class OrderAdminModel(admin.ModelAdmin):
    inlines = [OrderedActivityInlineModel]


admin.site.register(models.Transaction)
admin.site.register(models.ImageGallery, ImageGalleryAdminModel)
admin.site.register(models.Hotel, HotelAdminModel)
admin.site.register(models.RentingCenter, RentingCenterAdminModel)
admin.site.register(models.MedicalFacility, MedicalFacilityAdminModel)
admin.site.register(models.Trip, TripAdminModel)
admin.site.register(models.Order, OrderAdminModel)
