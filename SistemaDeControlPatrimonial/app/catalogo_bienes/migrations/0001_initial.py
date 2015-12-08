# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contabilidad', '0001_initial'),
        ('institucion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CatalogoDeBien',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=128)),
                ('descripcion', models.TextField()),
            ],
            options={
                'db_table': 'CatalogoDeBien',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Clase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=128)),
                ('descripcion', models.TextField()),
                ('is_active', models.BooleanField(default=True)),
                ('create_at', models.DateTimeField(auto_now=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('workstation_name', models.CharField(max_length=64, null=True, blank=True)),
                ('workstation_ip', models.CharField(max_length=64, null=True, blank=True)),
            ],
            options={
                'db_table': 'Clase',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=128)),
                ('descripcion', models.TextField()),
                ('is_active', models.BooleanField(default=True)),
                ('create_at', models.DateTimeField(auto_now=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('workstation_name', models.CharField(max_length=64, null=True, blank=True)),
                ('workstation_ip', models.CharField(max_length=64, null=True, blank=True)),
                ('institucion', models.ForeignKey(to='institucion.Institucion')),
                ('local', models.ForeignKey(to='institucion.Local')),
                ('sede', models.ForeignKey(to='institucion.Sede')),
                ('user', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'db_table': 'Grupo',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='clase',
            name='grupo',
            field=models.ForeignKey(to='catalogo_bienes.Grupo'),
        ),
        migrations.AddField(
            model_name='clase',
            name='institucion',
            field=models.ForeignKey(to='institucion.Institucion'),
        ),
        migrations.AddField(
            model_name='clase',
            name='local',
            field=models.ForeignKey(to='institucion.Local'),
        ),
        migrations.AddField(
            model_name='clase',
            name='sede',
            field=models.ForeignKey(to='institucion.Sede'),
        ),
        migrations.AddField(
            model_name='clase',
            name='user',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='catalogodebien',
            name='clase',
            field=models.ForeignKey(to='catalogo_bienes.Clase'),
        ),
        migrations.AddField(
            model_name='catalogodebien',
            name='cuenta_contable_divisionaria',
            field=models.ForeignKey(to='contabilidad.CuentaContableDivisionaria'),
        ),
        migrations.AddField(
            model_name='catalogodebien',
            name='grupo',
            field=models.ForeignKey(to='catalogo_bienes.Grupo'),
        ),
    ]
