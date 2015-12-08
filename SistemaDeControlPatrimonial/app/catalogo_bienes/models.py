from django.db import models
from django.contrib.auth.models import User
from SistemaDeControlPatrimonial.app.institucion.models import Institucion
from SistemaDeControlPatrimonial.app.institucion.models import Sede
from SistemaDeControlPatrimonial.app.institucion.models import Local
from SistemaDeControlPatrimonial.app.institucion.models import Ambiente
from SistemaDeControlPatrimonial.app.contabilidad.models import CuentaContableDivisionaria



"""Patrimonio"""
class Grupo(models.Model):
    institucion = models.ForeignKey(Institucion)
    sede = models.ForeignKey(Sede)
    local = models.ForeignKey(Local)
    nombre = models.CharField(max_length=128)
    descripcion = models.TextField()
    is_active = models.BooleanField(default=True)
    create_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User,blank=True, null=True)
    workstation_name = models.CharField(max_length=64,blank=True, null=True)
    workstation_ip = models.CharField(max_length=64,blank=True, null=True)

    def __str__(self):
        return '{0}'.format(self.nombre)

    class Meta:
        managed = True
        db_table = 'Grupo'


class Clase(models.Model):
    institucion = models.ForeignKey(Institucion)
    sede = models.ForeignKey(Sede)
    local = models.ForeignKey(Local)
    grupo = models.ForeignKey(Grupo)
    nombre = models.CharField(max_length=128)
    descripcion = models.TextField()
    is_active = models.BooleanField(default=True)
    create_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User,blank=True, null=True)
    workstation_name = models.CharField(max_length=64,blank=True, null=True)
    workstation_ip = models.CharField(max_length=64,blank=True, null=True)

    def __str__(self):
        return '{0}'.format(self.nombre)

    class Meta:
        managed = True
        db_table = 'Clase'


class CatalogoDeBien(models.Model):
    nombre = models.CharField(max_length=128)
    descripcion = models.TextField()
    grupo = models.ForeignKey(Grupo)
    clase = models.ForeignKey(Clase)
    cuenta_contable_divisionaria = models.ForeignKey(CuentaContableDivisionaria)

    def __str__(self):
        return '{0}'.format(self.nombre)

    class Meta:
        managed = True
        db_table = 'CatalogoDeBien'
