from django import forms
from route.models import PlatformType, RoutePlatform, RoutePoint, Route, BusModel


class BusModelForm(forms.ModelForm):
    class Meta:
        model = BusModel
        exclude = ()


class RouteForm(forms.ModelForm):
    class Meta:
        model = Route
        exclude = ('state',)


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
