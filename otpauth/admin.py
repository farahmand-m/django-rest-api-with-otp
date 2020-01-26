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


class OTPAdminModel(admin.ModelAdmin):
    fields = ('account', 'key', 'latest')
    readonly_fields = ('account', 'latest')


admin.site.unregister(Group)  # Not used
admin.site.register(auth_models.Corporation)
admin.site.register(auth_models.User, UserAdminModel)
admin.site.register(auth_models.OTP, OTPAdminModel)
