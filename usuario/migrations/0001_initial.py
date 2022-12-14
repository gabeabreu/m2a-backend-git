# Generated by Django 3.2.7 on 2022-06-26 21:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('uf', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubUserBaseMixin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200, unique=True)),
                ('password', models.CharField(max_length=200)),
                ('ativo', models.BooleanField()),
                ('email', models.EmailField(max_length=254)),
                ('tipo', models.IntegerField(choices=[(1, 'Administrator'), (2, 'Consultor'), (3, 'Empresa'), (4, 'Empresa Master')])),
            ],
        ),
        migrations.CreateModel(
            name='Adm',
            fields=[
                ('subuserbasemixin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='usuario.subuserbasemixin')),
                ('nome', models.CharField(max_length=100)),
                ('sobrenome', models.CharField(max_length=100)),
                ('cpf', models.CharField(max_length=30, unique=True)),
            ],
            bases=('usuario.subuserbasemixin',),
        ),
        migrations.AddField(
            model_name='subuserbasemixin',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuario.usuario'),
        ),
        migrations.CreateModel(
            name='Consultor',
            fields=[
                ('subuserbasemixin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='usuario.subuserbasemixin')),
                ('nome', models.CharField(max_length=100)),
                ('sobrenome', models.CharField(max_length=100)),
                ('cpf', models.CharField(max_length=30, unique=True)),
                ('telefone', models.CharField(max_length=13)),
                ('celular', models.CharField(max_length=13)),
                ('formacao', models.CharField(max_length=45)),
                ('uf', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uf.uf')),
            ],
            bases=('usuario.subuserbasemixin',),
        ),
    ]
