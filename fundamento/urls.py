from rest_framework import routers
from fundamento.views import FundamentoViewSet
from django.urls import path, include


router = routers.DefaultRouter()
router.register(r'fundamento', FundamentoViewSet, basename='fundamento')

urlpatterns = [
    path("", include(router.urls)),
]
