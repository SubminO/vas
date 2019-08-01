from django.contrib import admin

from .models import PlatformType, Route,RoutePlatform, RoutePoint


admin.site.register((PlatformType, Route,RoutePlatform, RoutePoint))
