from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from resposta.models import Resposta
from resposta.serializer import RespostaSerializer


# Create your views here.
class RespostaViewSet(viewsets.ModelViewSet):
    queryset = Resposta.objects.filter()
    serializer_class = RespostaSerializer
    model_class = Resposta
    user_class = True
    # permission_classes = (IsAuthenticated,)
    filter_fields = '__all__'