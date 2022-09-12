from rest_framework import serializers
from empresa.models import Empresa, EmpresaMaster


class EmpresaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Empresa
        fields = "__all__"


class EmpresaMasterSerializer(serializers.ModelSerializer):

    class Meta:
        model = EmpresaMaster
        fields = "__all__"
