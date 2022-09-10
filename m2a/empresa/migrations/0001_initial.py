# Generated by Django 3.2.7 on 2022-06-26 21:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('segmento', '0001_initial'),
        ('endereco', '0001_initial'),
        ('tipo_industria', '0001_initial'),
        ('setor', '0001_initial'),
        ('usuario', '0001_initial'),
        ('valor_arrecadacao', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmpresaMaster',
            fields=[
                ('subuserbasemixin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='usuario.subuserbasemixin')),
                ('cnpj', models.CharField(max_length=14, unique=True)),
                ('razao_social', models.CharField(max_length=2000)),
                ('fantasia', models.CharField(max_length=100)),
                ('num_empregados', models.IntegerField()),
                ('dt_ano_inicio', models.DateField()),
                ('telefone', models.CharField(max_length=13)),
                ('inscricao_estadual', models.CharField(blank=True, max_length=45)),
                ('fax', models.CharField(blank=True, max_length=60)),
                ('celular', models.CharField(blank=True, max_length=13)),
                ('ds_negocio', models.CharField(blank=True, max_length=2000)),
                ('missao', models.CharField(blank=True, max_length=500)),
                ('visao', models.CharField(blank=True, max_length=500)),
                ('valores', models.CharField(blank=True, max_length=500)),
                ('projeto', models.CharField(blank=True, max_length=500)),
                ('resp_nome', models.CharField(max_length=100)),
                ('resp_sobrenome', models.CharField(max_length=100)),
                ('resp_email', models.EmailField(max_length=254)),
                ('resp_sexo', models.CharField(max_length=100)),
                ('resp_formacao_academica', models.CharField(max_length=100)),
                ('endereco', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='endereco.endereco')),
                ('segmento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='segmento.segmento')),
                ('setor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='setor.setor')),
                ('tipo_industria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tipo_industria.tipoindustria')),
                ('valor_arrecadacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='valor_arrecadacao.valorarrecadacao')),
            ],
            bases=('usuario.subuserbasemixin',),
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cnpj', models.CharField(max_length=14, unique=True)),
                ('razao_social', models.CharField(max_length=2000)),
                ('fantasia', models.CharField(max_length=100)),
                ('num_empregados', models.IntegerField()),
                ('dt_ano_inicio', models.DateField()),
                ('telefone', models.CharField(max_length=13)),
                ('inscricao_estadual', models.CharField(blank=True, max_length=45)),
                ('fax', models.CharField(blank=True, max_length=60)),
                ('celular', models.CharField(blank=True, max_length=13)),
                ('ds_negocio', models.CharField(blank=True, max_length=2000)),
                ('missao', models.CharField(blank=True, max_length=500)),
                ('visao', models.CharField(blank=True, max_length=500)),
                ('valores', models.CharField(blank=True, max_length=500)),
                ('projeto', models.CharField(blank=True, max_length=500)),
                ('resp_nome', models.CharField(max_length=100)),
                ('resp_sobrenome', models.CharField(max_length=100)),
                ('resp_email', models.EmailField(max_length=254)),
                ('resp_sexo', models.CharField(max_length=100)),
                ('resp_formacao_academica', models.CharField(max_length=100)),
                ('usuario', models.IntegerField(unique=True)),
                ('endereco', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='endereco.endereco')),
                ('master', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empresa.empresamaster')),
                ('segmento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='segmento.segmento')),
                ('setor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='setor.setor')),
                ('tipo_industria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tipo_industria.tipoindustria')),
                ('valor_arrecadacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='valor_arrecadacao.valorarrecadacao')),
            ],
        ),
    ]
