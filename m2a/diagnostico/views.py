from rest_framework import viewsets

from diagnostico.models import Diagnostico
from diagnostico.serializer import DiagnosticoSerializer


# Create your views here.
class DiagnosticoViewSet(viewsets.ModelViewSet):
    queryset = Diagnostico.objects.filter()
    serializer_class = DiagnosticoSerializer
    model_class = Diagnostico
    user_class = True
    filter_fields = '__all__'
