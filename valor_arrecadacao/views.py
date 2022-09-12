from rest_framework import viewsets
from valor_arrecadacao.serializer import ValorArrecadacaoSerializer
from valor_arrecadacao.models import ValorArrecadacao


# Create your views here.
class ValorArrecadacaoViewSet(viewsets.ModelViewSet):
    queryset = ValorArrecadacao.objects.filter()
    serializer_class = ValorArrecadacaoSerializer
    model_class = ValorArrecadacao
    user_class = True
    filter_fields = '__all__'