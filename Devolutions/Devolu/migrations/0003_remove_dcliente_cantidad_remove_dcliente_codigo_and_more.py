# Generated by Django 4.0.4 on 2022-12-07 20:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Devolu', '0002_rename_devolucioncliente_dcliente'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dcliente',
            name='cantidad',
        ),
        migrations.RemoveField(
            model_name='dcliente',
            name='codigo',
        ),
        migrations.RemoveField(
            model_name='dcliente',
            name='comentario',
        ),
        migrations.RemoveField(
            model_name='dcliente',
            name='distribuidor',
        ),
        migrations.RemoveField(
            model_name='dcliente',
            name='nombrevendedor',
        ),
        migrations.RemoveField(
            model_name='dcliente',
            name='producto',
        ),
        migrations.CreateModel(
            name='devolucion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.CharField(max_length=100)),
                ('producto', models.CharField(max_length=100)),
                ('codigo', models.CharField(max_length=100)),
                ('nombre_vendedor', models.CharField(max_length=100)),
                ('distribuidor', models.CharField(max_length=100)),
                ('comentario', models.CharField(max_length=100)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Devolu.dcliente')),
            ],
        ),
    ]
