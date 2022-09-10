from rest_framework import routers
from tipo_industria.views import TipoIndustriaViewSet
from django.urls import path, include


router = routers.DefaultRouter()
router.register(r'tipo_industria', TipoIndustriaViewSet,
                basename='tipo_industria')

urlpatterns = [
    path("", include(router.urls)),
]
