from rest_framework import routers
from questionario.views import QuestionarioViewSet, EmpresaQuestionarioViewSet
from django.urls import path, include


router = routers.DefaultRouter()
router.register(r'questionario', QuestionarioViewSet, basename='questionario')
router.register(r'empresa_questionario', EmpresaQuestionarioViewSet,
                basename='empresa_questionario')

urlpatterns = [
    path("", include(router.urls)),
]
