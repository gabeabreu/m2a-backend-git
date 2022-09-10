from rest_framework import serializers
from uf.models import Uf


class UfSerializer(serializers.ModelSerializer):
    class Meta:
        model = Uf
        fields = "__all__"
