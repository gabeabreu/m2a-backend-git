from rest_framework import routers
from usuario.views import UsuarioViewSet, AdmViewSet, ConsultorViewSet
from django.urls import path, include


router = routers.DefaultRouter()
router.register(r'usuario', UsuarioViewSet, basename='usuario')
router.register(r'adm', AdmViewSet, basename='adm')
router.register(r'consultor', ConsultorViewSet, basename='consultor')

urlpatterns = [
    path("", include(router.urls)),
]
