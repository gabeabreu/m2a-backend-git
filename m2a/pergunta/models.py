from django.db import models
from fundamento.models import Fundamento
from resposta.models import Resposta


# Create your models here.
class Pergunta(models.Model):
    texto_pergunta = models.CharField(max_length=5000)
    conceito = models.CharField(max_length=5000, blank=True)
    objetivo = models.CharField(max_length=5000, blank=True)
    fundamento = models.ForeignKey(Fundamento, on_delete=models.CASCADE)
    respostas = models.ManyToManyField(Resposta)
