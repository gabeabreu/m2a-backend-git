from rest_framework import serializers
from pergunta.models import Pergunta
from resposta.serializer import RespostaSerializer
from resposta.models import Resposta


class PerguntaSerializer(serializers.ModelSerializer):
    formatadas = serializers.SerializerMethodField()

    class Meta:
        model = Pergunta
        fields = "__all__"

    def get_formatadas(self, pergunta):
        return RespostaSerializer(pergunta.respostas.all(), many=True).data
