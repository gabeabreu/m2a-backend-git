from django.db import models


# Create your models here.
class Resposta(models.Model):
    texto_resposta = models.CharField(max_length=5000)
    valor = models.IntegerField()
