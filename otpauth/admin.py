from django.contrib import admin
from django.contrib.auth.models import Group

from . import models as auth_models


class UserAdminModel(admin.ModelAdmin):
    fieldsets = (
        ('Authentication', {
            'fields': ['phone_number', 'otp_key']
        }),
        ('Account Options', {
            'fields': ['user_type', 'is_active']
        }),
        ('Corporation Settings', {
            'fields': ['corporation']
        }),
        ('Personal Details', {
            'fields': ['avatar', 'first_name', 'last_name', 'country']
        })
    )


admin.site.unregister(Group)
admin.site.register(auth_models.User, UserAdminModel)
