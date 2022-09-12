from rest_framework import viewsets
from endereco.serializer import EnderecoSerializer
from endereco.models import Endereco


# Create your views here.
class EnderecoViewSet(viewsets.ModelViewSet):
    queryset = Endereco.objects.filter()
    serializer_class = EnderecoSerializer
    model_class = Endereco
    user_class = True
    filter_fields = '__all__'
