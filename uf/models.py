from django.db import models


# Create your models here.
class Uf(models.Model):
    sg_uf = models.CharField(max_length=2)
    nome_uf = models.CharField(max_length=20)
