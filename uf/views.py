from rest_framework import viewsets
from uf.serializer import UfSerializer
from uf.models import Uf


# Create your views here.
class UfViewSet(viewsets.ModelViewSet):
    queryset = Uf.objects.filter()
    serializer_class = UfSerializer
    model_class = Uf
    user_class = True
    filter_fields = '__all__'
