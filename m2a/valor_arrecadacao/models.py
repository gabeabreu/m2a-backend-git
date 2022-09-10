from django.db import models


# Create your models here.
class ValorArrecadacao(models.Model):
    tipo_arrecadacao = models.CharField(max_length=100)
