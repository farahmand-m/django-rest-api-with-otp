import pyotp
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django_countries.fields import CountryField

from app.models import Corporation


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

    phone_number = models.CharField(max_length=20, db_index=True, unique=True)

    USERNAME_FIELD = 'phone_number'

    is_active = models.BooleanField(default=True)
    otp_key = models.CharField(max_length=100, blank=True, null=True, verbose_name='OTP Generation Key')

    USER_TYPES = (
        ('A', 'Administrator'),
        ('T', 'Tourist'),
        ('O', 'Operator'),
        ('M', 'Manager')
    )

    user_type = models.CharField(max_length=1, choices=USER_TYPES, default='T')

    @property
    def is_staff(self):
        return self.user_type == 'A'

    @is_staff.setter
    def is_staff(self, value):
        if value is True:
            self.user_type = 'A'

    corporation = models.ForeignKey(Corporation, on_delete=models.CASCADE, null=True, blank=True)

    first_name = models.TextField(blank=True)
    last_name = models.TextField(blank=True)
    avatar = models.ImageField(null=True, blank=True)
    country = CountryField(null=True, blank=True)

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
