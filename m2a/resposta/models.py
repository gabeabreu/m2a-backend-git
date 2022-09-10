from django.db import models


# Create your models here.
class Resposta(models.Model):
    texto_resposta = models.CharField(max_length=45)
    valor = models.IntegerField()
