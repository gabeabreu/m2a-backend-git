from django.db import models
from endereco.models import Endereco
from segmento.models import Segmento
from setor.models import Setor
from tipo_industria.models import TipoIndustria
from valor_arrecadacao.models import ValorArrecadacao
from usuario.models import SubUserBaseMixin, Usuario
from django.contrib.auth.models import User


class EmpresaMaster(SubUserBaseMixin):
    cnpj = models.CharField(max_length=14, unique=True)
    razao_social = models.CharField(max_length=2000)
    fantasia = models.CharField(max_length=100)
    num_empregados = models.IntegerField()
    dt_ano_inicio = models.DateField()
    telefone = models.CharField(max_length=13)
    inscricao_estadual = models.CharField(max_length=45, blank=True)
    fax = models.CharField(max_length=60, blank=True)
    celular = models.CharField(max_length=13, blank=True)
    ds_negocio = models.CharField(max_length=2000, blank=True)
    missao = models.CharField(max_length=500, blank=True)
    visao = models.CharField(max_length=500, blank=True)
    valores = models.CharField(max_length=500, blank=True)
    projeto = models.CharField(max_length=500, blank=True)

    resp_nome = models.CharField(max_length=100)
    resp_sobrenome = models.CharField(max_length=100)
    resp_email = models.EmailField()
    resp_sexo = models.CharField(max_length=100)
    resp_formacao_academica = models.CharField(max_length=100)

    segmento = models.ForeignKey(Segmento, on_delete=models.CASCADE)
    setor = models.ForeignKey(Setor, on_delete=models.CASCADE)
    tipo_industria = models.ForeignKey(TipoIndustria, on_delete=models.CASCADE)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)
    valor_arrecadacao = models.ForeignKey(ValorArrecadacao,
                                          on_delete=models.CASCADE)


class Empresa(models.Model):
    cnpj = models.CharField(max_length=14, unique=True)
    razao_social = models.CharField(max_length=2000)
    fantasia = models.CharField(max_length=100)
    num_empregados = models.IntegerField()
    dt_ano_inicio = models.DateField()
    telefone = models.CharField(max_length=13)
    inscricao_estadual = models.CharField(max_length=45, blank=True)
    fax = models.CharField(max_length=60, blank=True)
    celular = models.CharField(max_length=13, blank=True)
    ds_negocio = models.CharField(max_length=2000, blank=True)
    missao = models.CharField(max_length=500, blank=True)
    visao = models.CharField(max_length=500, blank=True)
    valores = models.CharField(max_length=500, blank=True)
    projeto = models.CharField(max_length=500, blank=True)

    resp_nome = models.CharField(max_length=100)
    resp_sobrenome = models.CharField(max_length=100)
    resp_email = models.EmailField()
    resp_sexo = models.CharField(max_length=100)
    resp_formacao_academica = models.CharField(max_length=100)

    segmento = models.ForeignKey(Segmento, on_delete=models.CASCADE)
    setor = models.ForeignKey(Setor, on_delete=models.CASCADE)
    tipo_industria = models.ForeignKey(TipoIndustria, on_delete=models.CASCADE)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)
    valor_arrecadacao = models.ForeignKey(ValorArrecadacao,
                                          on_delete=models.CASCADE)
    master = models.ForeignKey(EmpresaMaster, on_delete=models.CASCADE)
    usuario = models.IntegerField(unique=True)

    def delete(self, using=None, keep_parents=False):
        super().delete(using=None, keep_parents=False)
        id_ = self.usuario
        username = Usuario.objects.filter(id=id_).username
        Usuario.objects.filter(username=username).delete()
        User.objects.filter(username=username).delete()
