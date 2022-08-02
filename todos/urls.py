from rest_framework.routers import SimpleRouter

from .views import ListViewSet, UserViewSet


router = SimpleRouter()
router.register("users", UserViewSet, basename="users")
router.register("", ListViewSet, basename="todos")

urlpatterns = router.urls
