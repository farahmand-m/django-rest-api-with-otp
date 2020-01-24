from django.urls import path
from rest_framework.authtoken import views as token_views

from otpauth import views

urlpatterns = [
    path('request/', views.request_otp, name='request_otp'),
    path('auth/', token_views.obtain_auth_token, name='otp_auth')
]
