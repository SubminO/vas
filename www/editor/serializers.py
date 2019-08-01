from rest_framework.serializers import ModelSerializer

from editor import models


class RouteSerializer(ModelSerializer):
    class Meta:
        model = models.Route
        fields = ['id','name', 'description', 'platforms']


class PlatformTypeSerializer(ModelSerializer):
    class Meta:
        model = models.PlatformType
        fields = ['id','name', 'description']
