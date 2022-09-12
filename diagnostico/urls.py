from rest_framework import routers
from diagnostico.views import DiagnosticoViewSet
from django.urls import path, include


router = routers.DefaultRouter()
router.register(r'diagnostico', DiagnosticoViewSet, basename='diagnostico')

urlpatterns = [
    path("", include(router.urls)),
]
