# Generated by Django 2.1.4 on 2019-03-22 19:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthUserExtraFields',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='extra_fields', serialize=False, to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128)),
            ],
        ),
    ]
