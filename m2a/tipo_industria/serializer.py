from rest_framework import serializers
from tipo_industria.models import TipoIndustria


class TipoIndustriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoIndustria
        fields = "__all__"
