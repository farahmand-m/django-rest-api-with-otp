# Generated by Django 3.0.2 on 2020-01-08 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('otpauth', '0002_auto_20200108_0743'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='latest_otp',
            field=models.TextField(blank=True),
        ),
    ]