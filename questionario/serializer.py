from rest_framework import serializers
from questionario.models import Questionario, EmpresaQuestionario


class QuestionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questionario
        fields = "__all__"


class EmpresaQuestionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmpresaQuestionario
        fields = "__all__"
