from django.db import models
from uf.models import Uf
from django.contrib.auth.models import User

# Create your models here.
class Usuario(models.Model):

    class UserChoices(models.IntegerChoices):
        ADMINISTRATOR = 1
        CONSULTOR = 2
        EMPRESA = 3
        EMPRESA_MASTER = 4

    username = models.CharField(max_length=200, null=False, unique=True)
    password = models.CharField(max_length=200, null=False)
    ativo = models.BooleanField()
    email = models.EmailField()
    tipo = models.IntegerField(choices=UserChoices.choices)


class SubUserBaseMixin(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def delete(self, using=None, keep_parents=False):
        super().delete(using=None, keep_parents=False)
        username = self.usuario.username
        Usuario.objects.filter(username=username).delete()
        User.objects.filter(username=username).delete()


class Adm(SubUserBaseMixin):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=30, unique=True, null=False)


class Consultor(SubUserBaseMixin):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=30, unique=True, null=False)
    telefone = models.CharField(max_length=13, null=False)
    celular = models.CharField(max_length=13, null=False)
    formacao = models.CharField(max_length=45, null=False)
    uf = models.ForeignKey(Uf, on_delete=models.CASCADE)
