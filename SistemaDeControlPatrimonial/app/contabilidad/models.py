from django.db import models


"""Contabilidad"""
class CuentaContable(models.Model):
    nombre = models.CharField(max_length=128)
    numero_cuenta = models.IntegerField()

    def __str__(self):
        return '{0}'.format(self.nombre)

    class Meta:
        managed = True
        db_table = 'CuentaContable'


class SubCuentaContable(models.Model):
    nombre = models.CharField(max_length=128)
    numero_cuenta = models.IntegerField()
    cuenta_contable = models.ForeignKey(CuentaContable)

    def __str__(self):
        return '{0}'.format(self.nombre)

    class Meta:
        managed = True
        db_table = 'SubCuentaContable'


class CuentaContableDivisionaria(models.Model):
    nombre = models.CharField(max_length=128)
    numero_cuenta = models.IntegerField()
    sub_cuenta_contable = models.ForeignKey(SubCuentaContable)
    depreciacion = models.BooleanField()
    cuenta_depreciacion = models.IntegerField()

    def __str__(self):
        return '{0}'.format(self.nombre)

    class Meta:
        managed = True
        db_table = 'CuentaContableDivisionaria'
