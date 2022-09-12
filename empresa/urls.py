from rest_framework import routers
from empresa.views import EmpresaViewSet, EmpresaMasterViewSet
from django.urls import path, include


router = routers.DefaultRouter()
router.register(r'empresa', EmpresaViewSet, basename='empresa')
router.register(r'empresa_master', EmpresaMasterViewSet,
                basename='empresa_master')

urlpatterns = [
    path("", include(router.urls)),
]
