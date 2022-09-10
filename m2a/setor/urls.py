from rest_framework import routers
from setor.views import SetorViewSet
from django.urls import path, include


router = routers.DefaultRouter()
router.register(r'setor', SetorViewSet, basename='setor')

urlpatterns = [
    path("", include(router.urls)),
]
