from rest_framework import routers
from resposta.views import RespostaViewSet
from django.urls import path, include


router = routers.DefaultRouter()
router.register(r'resposta', RespostaViewSet, basename='resposta')

urlpatterns = [
    path("", include(router.urls)),
]
