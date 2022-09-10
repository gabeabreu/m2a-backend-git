from django.db import models
from uf.models import Uf


class Endereco(models.Model):
    cep = models.CharField(max_length=8)
    logradouro = models.CharField(max_length=45, blank=True)
    bairro = models.CharField(max_length=45, blank=True)
    cidade = models.CharField(max_length=45, blank=True)
    complemento = models.CharField(max_length=45, blank=True)
    uf = models.ForeignKey(Uf, on_delete=models.CASCADE)
