from django.db import models


# Create your models here.
class TipoIndustria(models.Model):
    ds_tipo_industria = models.CharField(max_length=60)
