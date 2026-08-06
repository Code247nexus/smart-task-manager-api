from rest_framework.routers import DefaultRouter
from .views import TaskViewSet
from drf_yasg import openapi
router = DefaultRouter()

router.register("", TaskViewSet, basename="tasks")

urlpatterns = router.urls