from django import forms
from django.forms import modelformset_factory

from route.models import PlatformType, RoutePlatform, Route, BusModel, RoutePoint


class BusModelForm(forms.ModelForm):
    class Meta:
        model = BusModel
        exclude = ()


class RouteForm(forms.ModelForm):
    class Meta:
        model = Route
        exclude = ('state',)
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите навзание маршрута'
            })
        }


class RoutePlatformForm(forms.ModelForm):
    class Meta:
        model = RoutePlatform
        fields = ('name', 'description', 'latitude', 'longitude')
        widgets = {
            'latitude': forms.HiddenInput(),
            'longitude': forms.HiddenInput(),
        }


class PlatformTypeForm(forms.ModelForm):
    class Meta:
        model = PlatformType
        exclude = ()


class RouteSelectForm(forms.Form):
    route = forms.ChoiceField(label='Выберите маршрут', choices=Route.objects.all())
    widgets = {
        'route': forms.Select(attrs={
            'class': 'custom-select',
        })
    }


RoutePlatformFormset = modelformset_factory(
    RoutePoint,
    fields=('route_platform',),
    extra=1,
    widgets={
        'route_platform': forms.Select(attrs={
            'class': 'custom-select',
            'ini': 1,
            'placeholder': 'Выберите остановку'
        })
    }
)
