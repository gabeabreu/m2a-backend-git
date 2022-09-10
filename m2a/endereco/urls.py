from rest_framework import routers
from endereco.views import EnderecoViewSet
from django.urls import path, include


router = routers.DefaultRouter()
router.register(r'endereco', EnderecoViewSet, basename='endereco')

urlpatterns = [
    path("", include(router.urls)),
]
