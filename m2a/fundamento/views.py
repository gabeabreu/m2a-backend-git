from rest_framework import viewsets
from fundamento.serializer import FundamentoSerializer
from fundamento.models import Fundamento


# Create your views here.
class FundamentoViewSet(viewsets.ModelViewSet):
    queryset = Fundamento.objects.filter()
    serializer_class = FundamentoSerializer
    model_class = Fundamento
    user_class = True
    filter_fields = '__all__'
