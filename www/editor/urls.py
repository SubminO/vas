from rest_framework.routers import DefaultRouter

from editor.views import (
    RouteViewSet,
    PlatformTypeViewSet,
)

router = DefaultRouter()
router.register('routes', RouteViewSet)
router.register('platformtypes', PlatformTypeViewSet)

urlpatterns = router.urls
