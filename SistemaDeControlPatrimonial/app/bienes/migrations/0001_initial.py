# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo_bienes', '0001_initial'),
        ('proveedor', '0001_initial'),
        ('institucion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Almacen',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.TextField()),
                ('catalogo_de_bien', models.ForeignKey(to='catalogo_bienes.CatalogoDeBien')),
                ('proveedor', models.ForeignKey(to='proveedor.Proveedor')),
            ],
            options={
                'db_table': 'Almacen',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='AltaBien',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=128)),
                ('descripcion', models.TextField()),
            ],
            options={
                'db_table': 'AltaBien',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='AsignacionBien',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=128)),
                ('descripcion', models.TextField()),
                ('ambiente', models.ForeignKey(to='institucion.Ambiente')),
            ],
            options={
                'db_table': 'AsignacionBien',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='DisposicionBien',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=128)),
                ('descripcion', models.TextField()),
                ('disposicion', models.TextField(max_length=128)),
            ],
            options={
                'db_table': 'DisposicionBien',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Inventario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.TextField()),
                ('catalogo_de_bien', models.ForeignKey(to='catalogo_bienes.CatalogoDeBien')),
            ],
            options={
                'db_table': 'Inventario',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TipoAlmacen',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=15)),
                ('descripcion', models.TextField()),
            ],
            options={
                'db_table': 'TipoAlmacen',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TipoMedida',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=15)),
                ('descripcion', models.TextField()),
            ],
            options={
                'db_table': 'TipoMedida',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TrasladoBien',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=128)),
                ('descripcion', models.TextField()),
                ('destino', models.TextField(max_length=250)),
                ('inventario', models.ForeignKey(to='bienes.Inventario')),
                ('origen', models.ForeignKey(to='institucion.Ambiente')),
            ],
            options={
                'db_table': 'TrasladoBien',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='disposicionbien',
            name='inventario',
            field=models.ForeignKey(to='bienes.Inventario'),
        ),
        migrations.AddField(
            model_name='asignacionbien',
            name='inventario',
            field=models.ForeignKey(to='bienes.Inventario'),
        ),
        migrations.AddField(
            model_name='altabien',
            name='inventario',
            field=models.ForeignKey(to='bienes.Inventario'),
        ),
        migrations.AddField(
            model_name='almacen',
            name='tipo_almacen',
            field=models.ForeignKey(to='bienes.TipoAlmacen'),
        ),
        migrations.AddField(
            model_name='almacen',
            name='tipo_medida',
            field=models.ForeignKey(to='bienes.TipoMedida'),
        ),
    ]
