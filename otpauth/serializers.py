from rest_framework import serializers

from otpauth import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ['phone_number', 'first_name', 'last_name', 'avatar']
