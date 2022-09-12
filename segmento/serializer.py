from rest_framework import serializers
from segmento.models import Segmento


class SegmentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Segmento
        fields = "__all__"
