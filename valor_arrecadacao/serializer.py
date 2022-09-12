from rest_framework import serializers
from valor_arrecadacao.models import ValorArrecadacao


class ValorArrecadacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ValorArrecadacao
        fields = "__all__"
