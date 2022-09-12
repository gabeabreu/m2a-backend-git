from rest_framework import serializers
from diagnostico.models import Diagnostico


class DiagnosticoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diagnostico
        fields = "__all__"

