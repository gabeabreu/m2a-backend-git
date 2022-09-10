from django.db import models
from empresa.models import EmpresaMaster, Empresa
from pergunta.models import Pergunta
from resposta.models import Resposta


class EmpresaQuestionario(models.Model):
    empresa_master = models.ForeignKey(EmpresaMaster, null=True,
                                       on_delete=models.CASCADE)
    empresa = models.ForeignKey(Empresa, null=True, on_delete=models.CASCADE)
    tempo = models.IntegerField()


class Questionario(models.Model):
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)
    resposta = models.ForeignKey(Resposta, on_delete=models.CASCADE)
    empresa_questionario = models.ForeignKey(EmpresaQuestionario,
                                             on_delete=models.CASCADE)
