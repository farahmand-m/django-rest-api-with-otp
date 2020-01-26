import pyotp
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django_countries.fields import CountryField


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


class Corporation(models.Model):
    label = models.TextField()


class User(AbstractBaseUser, PermissionsMixin):

    objects = UserManager()

    phone_number = models.CharField(max_length=20, db_index=True, unique=True)

    USERNAME_FIELD = 'phone_number'

    is_active = models.BooleanField(default=True)

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

    @property
    def otp_key(self):
        otp, created = OTP.objects.get_or_create(account=self)
        if created:
            otp.key = pyotp.random_base32()
            otp.save()
        return otp.key

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

    def get_short_name(self):
        return self

    def authenticate(self, otp):
        t = pyotp.TOTP(self.otp_key, interval=180)
        return t.verify(otp)

    def set_password(self, raw_password):
        super().set_password(raw_password)
        otp = OTP.objects.get(account=self)
        otp.latest = raw_password
        otp.save()


class OTP(models.Model):
    """
    TODO: The 'latest' attr is only meant for logging during the development phase and must be deleted for deployment.
    """
    account = models.OneToOneField(User, on_delete=models.CASCADE)
    key = models.CharField(max_length=100, blank=True, null=True, verbose_name='OTP Generation Key')
    latest = models.CharField(max_length=5, null=True, blank=True, verbose_name='Latest OTP')

    def __str__(self):
        return '{}: {}'.format(self.account.phone_number, self.latest or 'Not set')

    class Meta:
        verbose_name = 'One-Time Password'
        verbose_name_plural = 'One-Time Passwords'
