from django.db import models
from django.contrib.auth.models import User
from SistemaDeControlPatrimonial.app.institucion.models import Institucion
from SistemaDeControlPatrimonial.app.institucion.models import Sede
from SistemaDeControlPatrimonial.app.institucion.models import Local
from SistemaDeControlPatrimonial.app.institucion.models import Ambiente
from SistemaDeControlPatrimonial.app.contabilidad.models import CuentaContableDivisionaria
from SistemaDeControlPatrimonial.app.catalogo_bienes.models import CatalogoDeBien
from SistemaDeControlPatrimonial.app.proveedor.models import Proveedor



class TipoMedida(models.Model):
    nombre = models.CharField(max_length=15)
    descripcion = models.TextField()

    def __str__(self):
        return '{0}'.format(self.nombre)

    class Meta:
        managed = True
        db_table = 'TipoMedida'


class TipoAlmacen(models.Model):
    nombre = models.CharField(max_length=15)
    descripcion = models.TextField()

    def __str__(self):
        return '{0}'.format(self.nombre)

    class Meta:
        managed = True
        db_table = 'TipoAlmacen'


class Almacen(models.Model):
    catalogo_de_bien = models.ForeignKey(CatalogoDeBien)
    proveedor = models.ForeignKey(Proveedor)
    tipo_medida = models.ForeignKey(TipoMedida)
    tipo_almacen = models.ForeignKey(TipoAlmacen)
    descripcion = models.TextField()

    def __str__(self):
        return '{0}'.format(self.catalogo_de_bien)

    class Meta:
        managed = True
        db_table = 'Almacen'


class Inventario(models.Model):
    catalogo_de_bien = models.ForeignKey(CatalogoDeBien)
    descripcion = models.TextField()

    def __str__(self):
        return '{0}'.format(self.catalogo_de_bien)

    class Meta:
        managed = True
        db_table = 'Inventario'


class AltaBien(models.Model):
    nombre = models.CharField(max_length=128)
    descripcion = models.TextField()
    inventario = models.ForeignKey(Inventario)

    def __str__(self):
        return '{0}'.format(self.nombre)

    class Meta:
        managed = True
        db_table = 'AltaBien'


class DisposicionBien(models.Model):
    nombre = models.CharField(max_length=128)
    descripcion = models.TextField()
    inventario = models.ForeignKey(Inventario)
    disposicion = models.TextField(max_length=128)

    def __str__(self):
        return '{0}'.format(self.nombre)

    class Meta:
        managed = True
        db_table = 'DisposicionBien'


class AsignacionBien(models.Model):
    nombre = models.CharField(max_length=128)
    descripcion = models.TextField()
    inventario = models.ForeignKey(Inventario)
    ambiente = models.ForeignKey(Ambiente)

    def __str__(self):
        return '{0}'.format(self.nombre)

    class Meta:
        managed = True
        db_table = 'AsignacionBien'



class TrasladoBien(models.Model):
    nombre = models.CharField(max_length=128)
    descripcion = models.TextField()
    inventario = models.ForeignKey(Inventario)
    origen = models.ForeignKey(Ambiente)
    destino = models.TextField(max_length=250)

    def __str__(self):
        return '{0}'.format(self.nombre)

    class Meta:
        managed = True
        db_table = 'TrasladoBien'
