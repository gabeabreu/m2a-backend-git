from rest_framework import routers
from segmento.views import SegmentoViewSet
from django.urls import path, include


router = routers.DefaultRouter()
router.register(r'segmento', SegmentoViewSet, basename='segmento')

urlpatterns = [
    path("", include(router.urls)),
]
