from rest_framework import serializers

from resposta.models import Resposta


class RespostaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Resposta
        fields = "__all__"
