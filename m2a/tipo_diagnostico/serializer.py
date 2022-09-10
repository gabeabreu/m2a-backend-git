from rest_framework import serializers
from tipo_diagnostico.models import TipoDiagnostico


class TipoDiagnosticoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoDiagnostico
        fields = "__all__"
