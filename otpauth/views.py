import pyotp
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets

from otpauth import models, serializers


@csrf_exempt
def request_otp(request):
    if not request.POST:
        return HttpResponse(status=200)
    phone_number = request.POST.get('phone_number', None)
    account, created = models.User.objects.get_or_create(phone_number=phone_number)
    if account.is_staff:
        return HttpResponse(status=403)
    timestamped_otp = pyotp.TOTP(account.otp_key, interval=180)
    otp = timestamped_otp.now()
    # TODO: The OTP needs to be sent to the user through SMS, etc.
    account.set_password(otp)
    account.save()
    return JsonResponse({'created': created})


class UserViewSet(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
