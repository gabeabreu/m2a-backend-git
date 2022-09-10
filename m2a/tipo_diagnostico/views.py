from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from tipo_diagnostico.models import TipoDiagnostico
from tipo_diagnostico.serializer import TipoDiagnosticoSerializer


# Create your views here.
class TipoDiagnosticoViewSet(viewsets.ModelViewSet):
    queryset = TipoDiagnostico.objects.filter()
    serializer_class = TipoDiagnosticoSerializer
    model_class = TipoDiagnostico
    user_class = True
    permission_classes = (IsAuthenticated,)
    filter_fields = '__all__'