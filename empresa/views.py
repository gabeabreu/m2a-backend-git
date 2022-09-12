from rest_framework import viewsets

from empresa.models import Empresa, EmpresaMaster
from empresa.serializer import EmpresaSerializer, EmpresaMasterSerializer
# Create your views here.
from endereco.models import Endereco
from endereco.serializer import EnderecoSerializer
from faturamento.models import Faturamento
from faturamento.serializer import FaturamentoSerializer

from segmento.models import Segmento
from segmento.serializer import SegmentoSerializer
from setor.models import Setor
from setor.serializer import SetorSerializer
from tipo_industria.models import TipoIndustria
from tipo_industria.serializer import TipoIndustriaSerializer
from valor_arrecadacao.models import ValorArrecadacao
from valor_arrecadacao.serializer import ValorArrecadacaoSerializer


class EmpresaMasterViewSet(viewsets.ModelViewSet):
    queryset = EmpresaMaster.objects.filter()
    serializer_class = EmpresaMasterSerializer
    model_class = EmpresaMaster
    user_class = True
    filter_fields = '__all__'

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        results = response.data['results']
        for empresa in results:
            empresa['segmento'] = SegmentoSerializer(
                Segmento.objects.get(id=empresa['segmento'])).data
            empresa['setor'] = SetorSerializer(
                Setor.objects.get(id=empresa['setor'])).data
            empresa['tipo_industria'] = TipoIndustriaSerializer(
                TipoIndustria.objects.get(id=empresa['tipo_industria'])).data
            empresa['endereco'] = EnderecoSerializer(
                Endereco.objects.get(id=empresa['endereco'])).data
            empresa['valor_arrecadacao'] = ValorArrecadacaoSerializer(
                ValorArrecadacao.objects.get(
                    id=empresa['valor_arrecadacao'])).data

        return response


class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.filter()
    serializer_class = EmpresaSerializer
    model_class = Empresa
    user_class = True
    filter_fields = '__all__'
