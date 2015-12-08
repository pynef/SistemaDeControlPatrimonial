# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('recursos_humanos', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('institucion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=64)),
                ('razon_social', models.CharField(max_length=128)),
                ('direccion_fiscal', models.CharField(max_length=64)),
                ('email', models.CharField(max_length=64)),
                ('ruc', models.CharField(max_length=15)),
                ('is_active', models.BooleanField(default=True)),
                ('create_at', models.DateTimeField(auto_now=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('workstation_name', models.CharField(max_length=64, null=True, blank=True)),
                ('workstation_ip', models.CharField(max_length=64, null=True, blank=True)),
                ('duenio', models.ForeignKey(to='recursos_humanos.Persona')),
                ('institucion', models.ForeignKey(to='institucion.Institucion')),
                ('user', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'db_table': 'Proveedor',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ProveedorTelefonos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numero', models.CharField(max_length=16)),
                ('operador', models.CharField(max_length=1)),
                ('descriptor', models.CharField(max_length=32, null=True, blank=True)),
                ('create_at', models.DateTimeField(auto_now=True, null=True)),
                ('institucion', models.ForeignKey(to='institucion.Institucion')),
                ('proveedor', models.ForeignKey(to='proveedor.Proveedor')),
            ],
            options={
                'db_table': 'ProveedorTelefonos',
                'managed': True,
            },
        ),
    ]
