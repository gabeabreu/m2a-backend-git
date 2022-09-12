from django.db import models
from empresa.models import Empresa, EmpresaMaster


# Create your models here.
class Faturamento(models.Model):
    dt_ano = models.DateField()
    valor = models.FloatField()
    empresa_master = models.ForeignKey(EmpresaMaster, null=True,
                                       on_delete=models.CASCADE)
    empresa = models.ForeignKey(Empresa, null=True, on_delete=models.CASCADE)
