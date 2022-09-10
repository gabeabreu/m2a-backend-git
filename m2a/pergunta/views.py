from rest_framework import viewsets

from pergunta.models import Pergunta
from pergunta.serializer import PerguntaSerializer


# Create your views here.
class PerguntaViewSet(viewsets.ModelViewSet):
    queryset = Pergunta.objects.filter()
    serializer_class = PerguntaSerializer
    model_class = Pergunta
    user_class = True
    # permission_classes = (IsAuthenticated,)
    filter_fields = '__all__'
