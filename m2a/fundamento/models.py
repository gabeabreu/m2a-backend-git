from django.db import models


# Create your models here.
class Fundamento(models.Model):
    nome_fundamento = models.CharField(max_length=60)
