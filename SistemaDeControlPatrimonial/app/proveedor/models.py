from django.db import models
from django.contrib.auth.models import User
from SistemaDeControlPatrimonial.app.institucion.models import Institucion
from SistemaDeControlPatrimonial.app.institucion.models import Sede
from SistemaDeControlPatrimonial.app.institucion.models import Local
from SistemaDeControlPatrimonial.app.institucion.models import Ambiente
from SistemaDeControlPatrimonial.app.recursos_humanos.models import Persona


"""Proveedores"""
class Proveedor(models.Model):
    institucion = models.ForeignKey(Institucion)
    nombre = models.CharField(max_length=64)
    razon_social = models.CharField(max_length=128)
    direccion_fiscal = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    ruc = models.CharField(max_length=15)
    duenio = models.ForeignKey(Persona)
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
        db_table = 'Proveedor'


class ProveedorTelefonos(models.Model):
    institucion = models.ForeignKey(Institucion)
    proveedor = models.ForeignKey(Proveedor)
    numero = models.CharField(max_length=16)
    operador = models.CharField(max_length=1)
    descriptor = models.CharField(max_length=32,blank=True, null=True)
    create_at = models.DateTimeField(auto_now=True,blank=True, null=True)

    def __str__(self):
        return '{0}'.format(self.numero)

    class Meta:
        managed = True
        db_table = 'ProveedorTelefonos'
