from rest_framework import serializers
from fundamento.models import Fundamento


class FundamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fundamento
        fields = "__all__"
