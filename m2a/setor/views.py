from rest_framework import viewsets
from setor.serializer import SetorSerializer
from setor.models import Setor


# Create your views here.
class SetorViewSet(viewsets.ModelViewSet):
    queryset = Setor.objects.filter()
    serializer_class = SetorSerializer
    model_class = Setor
    user_class = True
    filter_fields = '__all__'