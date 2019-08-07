from django import forms
from django.shortcuts import redirect
from phonenumber_field.formfields import PhoneNumberField
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from auth_user.models import AuthUserExtraFields


class UserCreateForm(UserCreationForm):
    phone_number = PhoneNumberField(required=True, label='Номер телефона', help_text='Номер телефона в формате +79372220202')

    class Meta:
        model = User
        fields = ("username", "phone_number", "password1", "password2")

    def save(self, commit=True):
        users = User.objects.all()
        if len(users) >= 1:
            return redirect('login')
        user = super(UserCreateForm, self).save(commit=False)
        # user.extra_fields = extra_fields
        # user.extra_field = self.cleaned_data["phone_number"]
        if commit:
            user.save()
            extra_fields = AuthUserExtraFields(phone_number=self.cleaned_data["phone_number"], user=user)
            extra_fields.save()
        return user


class SignUp(generic.CreateView):
    form_class = UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'