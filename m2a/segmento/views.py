from rest_framework import viewsets
from segmento.serializer import SegmentoSerializer
from segmento.models import Segmento


# Create your views here.
class SegmentoViewSet(viewsets.ModelViewSet):
    queryset = Segmento.objects.filter()
    serializer_class = SegmentoSerializer
    model_class = Segmento
    user_class = True
    filter_fields = '__all__'