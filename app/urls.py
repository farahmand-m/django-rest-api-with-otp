from django.urls import include, path
from rest_framework import routers

# from . import models as app_models

router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('rest/', include(router.urls))
]
