from rest_framework import routers
from pergunta.views import PerguntaViewSet
from django.urls import path, include


router = routers.DefaultRouter()
router.register(r'pergunta', PerguntaViewSet, basename='pergunta')

urlpatterns = [
    path("", include(router.urls)),
]
