from django.db import models


# Create your models here.
class TipoDiagnostico(models.Model):
    nome_tipo_diagnostico = models.CharField(max_length=45)
