import socket
from django.contrib import admin

from SistemaDeControlPatrimonial.app.contabilidad.models import CuentaContable
from SistemaDeControlPatrimonial.app.contabilidad.models import SubCuentaContable
from SistemaDeControlPatrimonial.app.contabilidad.models import CuentaContableDivisionaria

admin.site.register(CuentaContable)
admin.site.register(SubCuentaContable)
admin.site.register(CuentaContableDivisionaria)

