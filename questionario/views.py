from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from questionario.models import Questionario, EmpresaQuestionario
from questionario.serializer import QuestionarioSerializer, \
    EmpresaQuestionarioSerializer


# Create your views here.
class QuestionarioViewSet(viewsets.ModelViewSet):
    queryset = Questionario.objects.filter()
    serializer_class = QuestionarioSerializer
    model_class = Questionario
    user_class = True
    # permission_classes = (IsAuthenticated,)
    filter_fields = '__all__'

    @action(detail=False, methods=["get"], url_path="empresas",
            url_name="empresas")
    def play(self, request):
        """Play a playbook."""
        empresas_master = Questionario.objects.order_by().values('empresa_master').distinct()
        empresas = Questionario.objects.order_by().values('empresa').distinct()

        return Response({'master': list(empresas_master),
                         'empresa': list(empresas)}, 200)


class EmpresaQuestionarioViewSet(viewsets.ModelViewSet):
    queryset = EmpresaQuestionario.objects.filter()
    serializer_class = EmpresaQuestionarioSerializer
    model_class = EmpresaQuestionario
    user_class = True
    # permission_classes = (IsAuthenticated,)
    filter_fields = '__all__'
