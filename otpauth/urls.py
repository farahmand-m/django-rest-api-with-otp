from django.urls import path
from rest_framework.authtoken import views as token_views

from . import views as auth_views

urlpatterns = [
    path('request/', auth_views.request_otp, name='request_otp'),
    path('auth/', token_views.obtain_auth_token, name='otp_auth')
]
