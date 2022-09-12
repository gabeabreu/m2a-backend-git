from rest_framework import routers
from faturamento.views import FaturamentoViewSet
from django.urls import path, include


router = routers.DefaultRouter()
router.register(r'faturamento', FaturamentoViewSet, basename='faturamento')

urlpatterns = [
    path("", include(router.urls)),
]
