from route.models import (
    RoutePoint as BaseRoutePoint,
    RoutePlatform as BaseRoutePlatform,
    Route as BaseRoute,
    PlatformType as BasePlatformType
)


class RoutePoint(BaseRoutePoint):
    class Meta:
        proxy = True


class RoutePlatform(BaseRoutePlatform):
    class Meta:
        proxy = True


class Route(BaseRoute):
    class Meta:
        proxy = True


class PlatformType(BasePlatformType):
    class Meta:
        proxy = True
