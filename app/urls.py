from django.urls import include, path
from rest_framework import routers

from app import views
from otpauth import views as auth_views

router = routers.DefaultRouter()
router.register(r'users', auth_views.UserViewSet)
router.register(r'galleries', views.ImageGallery)
router.register(r'images', views.Image)
router.register(r'hotels', views.Hotel)
router.register(r'rooms', views.HotelRoom)
router.register(r'renting_centers', views.RentingCenter)
router.register(r'rentals', views.Rental)
router.register(r'medical_facility', views.MedicalFacility)
router.register(r'medical_service', views.MedicalService)
router.register(r'activity', views.Activity)
router.register(r'trip', views.Trip)
router.register(r'order', views.Order)
router.register(r'ordered_activity', views.OrderedActivity)


urlpatterns = [
    path('rest/', include(router.urls)),
    path('search/', views.search)
]
