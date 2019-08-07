from django import forms
from route.models import PlatformType, RoutePlatform, RoutePoint, Route


class RouteForm(forms.ModelForm):
    class Meta:
        model = Route
        exclude = ()


class RoutePlatformForm(forms.ModelForm):
    class Meta:
        model = RoutePlatform
        fields = ('name', 'description', 'type', 'latitude', 'longitude')
        widgets = {
            'latitude': forms.HiddenInput(),
            'longitude': forms.HiddenInput(),
        }


class PlatformTypeForm(forms.ModelForm):
    class Meta:
        model = PlatformType
        exclude = ()

# class RealEstateObjectTypeForm(forms.ModelForm):
#     class Meta:
#         model = RealEstateObjectTypeModel
#         exclude = ('date_created', 'date_updated')
#
#
# class RealEstateObjectForm(forms.ModelForm):
#     class Meta:
#         model = RealEstateObjectModel
#         exclude = ('date_created', 'date_updated')
#         widgets = {
#             'latitude': forms.HiddenInput(),
#             'longitude': forms.HiddenInput(),
#         }