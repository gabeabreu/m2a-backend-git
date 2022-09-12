from django.db import models


# Create your models here.
class Segmento(models.Model):
    ds_segmento = models.CharField(max_length=60)
