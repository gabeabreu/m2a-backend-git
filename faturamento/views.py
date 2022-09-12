from rest_framework import viewsets
from faturamento.serializer import FaturamentoSerializer
from faturamento.models import Faturamento


# Create your views here.
class FaturamentoViewSet(viewsets.ModelViewSet):
    queryset = Faturamento.objects.filter()
    serializer_class = FaturamentoSerializer
    model_class = Faturamento
    user_class = True
    filter_fields = '__all__'