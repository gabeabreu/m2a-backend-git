from rest_framework import viewsets
from tipo_industria.serializer import TipoIndustriaSerializer
from tipo_industria.models import TipoIndustria


# Create your views here.
class TipoIndustriaViewSet(viewsets.ModelViewSet):
    queryset = TipoIndustria.objects.filter()
    serializer_class = TipoIndustriaSerializer
    model_class = TipoIndustria
    user_class = True
    filter_fields = '__all__'