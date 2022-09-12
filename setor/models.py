from django.db import models


# Create your models here.
class Setor(models.Model):
    ds_setor = models.CharField(max_length=60)
