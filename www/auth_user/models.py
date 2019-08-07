from django.contrib.auth.models import User
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class AuthUserExtraFields(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='extra_fields', verbose_name='пользователь')
    phone_number = PhoneNumberField()

    def __str__(self):
        return "Пользователь: %s" % self.user.username
