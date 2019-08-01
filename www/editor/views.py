from rest_framework.viewsets import ModelViewSet

from editor.models import (
    Route,
    PlatformType
)
from editor.serializers import (
    RouteSerializer,
    PlatformTypeSerializer
)


class RouteViewSet(ModelViewSet):
    serializer_class = RouteSerializer
    queryset = Route.objects.all()


class PlatformTypeViewSet(ModelViewSet):
    serializer_class = PlatformTypeSerializer
    queryset = PlatformType.objects.all()


