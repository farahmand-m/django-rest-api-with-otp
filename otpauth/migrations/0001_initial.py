# Generated by Django 3.0.2 on 2020-01-25 06:45

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Corporation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('phone_number', models.CharField(db_index=True, max_length=20, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('otp_key', models.CharField(blank=True, max_length=100, null=True, verbose_name='OTP Generation Key')),
                ('user_type', models.CharField(choices=[('A', 'Administrator'), ('T', 'Tourist'), ('O', 'Operator'), ('M', 'Manager')], default='T', max_length=1)),
                ('first_name', models.TextField(blank=True)),
                ('last_name', models.TextField(blank=True)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='')),
                ('country', django_countries.fields.CountryField(blank=True, max_length=2, null=True)),
                ('corporation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='otpauth.Corporation')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
        ),
    ]
