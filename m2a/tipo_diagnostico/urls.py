from rest_framework import routers
from tipo_diagnostico.views import TipoDiagnosticoViewSet
from django.urls import path, include


router = routers.DefaultRouter()
router.register(r'tipo_diagnostico', TipoDiagnosticoViewSet,
                basename='tipo_diagnostico')

urlpatterns = [
    path("", include(router.urls)),
]
