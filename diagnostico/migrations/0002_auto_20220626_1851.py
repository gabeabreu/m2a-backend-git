# Generated by Django 3.2.7 on 2022-06-26 21:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questionario', '0001_initial'),
        ('diagnostico', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='diagnostico',
            name='questionario',
        ),
        migrations.AddField(
            model_name='diagnostico',
            name='empresa_questionario',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='questionario.empresaquestionario'),
            preserve_default=False,
        ),
    ]
