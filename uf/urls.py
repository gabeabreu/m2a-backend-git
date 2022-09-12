from rest_framework import routers
from uf.views import UfViewSet
from django.urls import path, include


router = routers.DefaultRouter()
router.register(r'uf', UfViewSet, basename='uf')

urlpatterns = [
    path("", include(router.urls)),
]
