from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import Testconnectors134179ViewSet

router = DefaultRouter()
router.register(
    "testconnectors134179", Testconnectors134179ViewSet, basename="testconnectors134179"
)

urlpatterns = [
    path("connectors/", include(router.urls)),
]
