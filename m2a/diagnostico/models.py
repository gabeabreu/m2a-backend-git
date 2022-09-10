from django.db import models
from tipo_diagnostico.models import TipoDiagnostico
from questionario.models import EmpresaQuestionario
from usuario.models import Consultor
import datetime


# Create your models here.
class Diagnostico(models.Model):
    data = models.DateField(default=datetime.date.today)
    empresa_questionario = models.ForeignKey(EmpresaQuestionario, on_delete=models.CASCADE)
    consultor = models.ForeignKey(Consultor, on_delete=models.CASCADE)
    tipo_diagnostico = models.ForeignKey(TipoDiagnostico, on_delete=models.CASCADE)

