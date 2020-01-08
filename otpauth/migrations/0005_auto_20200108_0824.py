# Generated by Django 3.0.2 on 2020-01-08 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('otpauth', '0004_auto_20200108_0820'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='key',
        ),
        migrations.AddField(
            model_name='user',
            name='otp_key',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]