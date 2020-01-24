import pyotp
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models


class UserManager(BaseUserManager):

    def create_user(self, phone_number, password=None, **extra_fields):
        if phone_number is None:
            raise ValueError('Users are identified by their phone number and as a result, this field is mandatory.')
        user = self.model(phone_number=self.normalize_email(phone_number), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password, **extra_fields):
        if password is None:
            raise ValueError('You need to specify a password for superusers.')
        user = self.create_user(phone_number, password=password, **extra_fields)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):

    objects = UserManager()

    phone_number = models.TextField(db_index=True, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    otp_key = models.CharField(max_length=100, blank=True, null=True)
    latest_otp = models.TextField(blank=True)  # For testing purposes only. MUST be removed for production.

    USERNAME_FIELD = 'phone_number'

    first_name = models.TextField(blank=True)
    last_name = models.TextField(blank=True)
    avatar = models.ImageField(null=True, blank=True)

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def __str__(self):
        return self.phone_number

    def save(self, *args, **kwargs):
        if self.otp_key is None:
            self.otp_key = pyotp.random_base32()
        super().save(*args, **kwargs)

    def get_short_name(self):
        return self

    def authenticate(self, otp):
        t = pyotp.TOTP(self.otp_key, interval=180)
        return t.verify(otp)
