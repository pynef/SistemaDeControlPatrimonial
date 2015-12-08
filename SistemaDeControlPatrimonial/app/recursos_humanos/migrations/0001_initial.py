# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('institucion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=64)),
                ('descripcion', models.TextField(null=True, blank=True)),
                ('modulos', models.CharField(max_length=64, null=True, blank=True)),
                ('is_active', models.BooleanField(default=True)),
                ('create_at', models.DateTimeField(auto_now=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('workstation_name', models.CharField(max_length=64, null=True, blank=True)),
                ('workstation_ip', models.CharField(max_length=64, null=True, blank=True)),
                ('institucion', models.ForeignKey(to='institucion.Institucion')),
                ('local', models.ForeignKey(blank=True, to='institucion.Local', null=True)),
                ('sede', models.ForeignKey(to='institucion.Sede')),
                ('user', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'db_table': 'Area',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(max_length=32)),
                ('apellido_paterno', models.CharField(max_length=64)),
                ('apellido_materno', models.CharField(max_length=64)),
                ('nombres', models.CharField(max_length=64)),
                ('tipo_documento', models.CharField(max_length=1)),
                ('nro_documento', models.CharField(max_length=16)),
                ('fecha_nacimiento', models.DateField(null=True, blank=True)),
                ('ubigeo', models.CharField(max_length=6, null=True, blank=True)),
                ('direccion', models.CharField(max_length=128, null=True, blank=True)),
                ('referencia_direccion', models.TextField(null=True, blank=True)),
                ('estado_civil', models.CharField(max_length=1, null=True, blank=True)),
                ('genero', models.CharField(max_length=1)),
                ('grado_academico', models.CharField(max_length=1, null=True, blank=True)),
                ('imagen', models.CharField(max_length=256, null=True, blank=True)),
                ('img_documento', models.CharField(max_length=256, null=True, blank=True)),
                ('tipo', models.CharField(max_length=1, null=True, blank=True)),
                ('email', models.CharField(max_length=64)),
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
                'db_table': 'Persona',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='PersonaTelefono',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numero', models.CharField(max_length=16)),
                ('operador', models.CharField(max_length=1)),
                ('descriptor', models.CharField(max_length=32, null=True, blank=True)),
                ('create_at', models.DateTimeField(auto_now=True, null=True)),
                ('institucion', models.ForeignKey(to='institucion.Institucion')),
                ('local', models.ForeignKey(to='institucion.Local')),
                ('persona', models.ForeignKey(to='recursos_humanos.Persona')),
                ('sede', models.ForeignKey(to='institucion.Sede')),
            ],
            options={
                'db_table': 'PersonaTelefono',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Puesto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField(null=True, blank=True)),
                ('all_sedes', models.BooleanField()),
                ('is_active', models.BooleanField(default=True)),
                ('create_at', models.DateTimeField(auto_now=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('workstation_name', models.CharField(max_length=64, null=True, blank=True)),
                ('workstation_ip', models.CharField(max_length=64, null=True, blank=True)),
                ('area', models.ForeignKey(to='recursos_humanos.Area')),
                ('institucion', models.ForeignKey(to='institucion.Institucion')),
                ('local', models.ForeignKey(to='institucion.Local')),
                ('sede', models.ForeignKey(to='institucion.Sede')),
                ('user', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'db_table': 'Puesto',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Trabajador',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nro_aportantes', models.IntegerField(null=True, blank=True)),
                ('nro_dependientes', models.IntegerField(null=True, blank=True)),
                ('ingreso_familiar', models.DecimalField(null=True, max_digits=7, decimal_places=2, blank=True)),
                ('vivienda_tipo', models.CharField(max_length=64, null=True, blank=True)),
                ('vivienda_nro_habitantes', models.IntegerField(null=True, blank=True)),
                ('vivienda_servicio', models.CharField(max_length=256, null=True, blank=True)),
                ('vivienda_situacion', models.CharField(max_length=64, null=True, blank=True)),
                ('vivienda_material', models.CharField(max_length=64, null=True, blank=True)),
                ('enfermedades', models.CharField(max_length=256, null=True, blank=True)),
                ('enfermedad_cronica', models.CharField(max_length=256, null=True, blank=True)),
                ('discapacidad', models.CharField(max_length=256, null=True, blank=True)),
                ('alergia', models.CharField(max_length=256, null=True, blank=True)),
                ('objetivo_personal', models.TextField(null=True, blank=True)),
                ('tipo_contrato', models.CharField(max_length=128, null=True, blank=True)),
                ('tipo', models.CharField(max_length=1, null=True, blank=True)),
                ('is_active', models.BooleanField(default=True)),
                ('create_at', models.DateTimeField(auto_now=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('workstation_name', models.CharField(max_length=64, null=True, blank=True)),
                ('workstation_ip', models.CharField(max_length=64, null=True, blank=True)),
                ('ambiente', models.ForeignKey(to='institucion.Ambiente')),
                ('institucion', models.ForeignKey(to='institucion.Institucion')),
                ('local', models.ForeignKey(to='institucion.Local')),
                ('persona', models.ForeignKey(to='recursos_humanos.Persona')),
                ('sede', models.ForeignKey(to='institucion.Sede')),
                ('user', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'db_table': 'Trabajador',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TrabajadorPuesto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_active', models.BooleanField(default=True)),
                ('create_at', models.DateTimeField(auto_now=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('workstation_name', models.CharField(max_length=64, null=True, blank=True)),
                ('workstation_ip', models.CharField(max_length=64, null=True, blank=True)),
                ('institucion', models.ForeignKey(to='institucion.Institucion')),
                ('local', models.ForeignKey(to='institucion.Local')),
                ('puesto', models.ForeignKey(to='recursos_humanos.Puesto')),
                ('sede', models.ForeignKey(to='institucion.Sede')),
                ('trabajador', models.ForeignKey(to='recursos_humanos.Trabajador')),
                ('user', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'db_table': 'TrabajadorPuesto',
                'managed': True,
            },
        ),
    ]
