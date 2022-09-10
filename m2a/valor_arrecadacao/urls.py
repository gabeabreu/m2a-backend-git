from rest_framework import routers
from valor_arrecadacao.views import ValorArrecadacaoViewSet
from django.urls import path, include


router = routers.DefaultRouter()
router.register(r'valor_arrecadacao', ValorArrecadacaoViewSet,
                basename='valor_arrecadacao')

urlpatterns = [
    path("", include(router.urls)),
]
