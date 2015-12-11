import socket
from django.contrib import admin


from SistemaDeControlPatrimonial.app.Proveedor.models import Proveedor
from SistemaDeControlPatrimonial.app.Proveedor.models import ProveedorTelefonos


admin.site.register(Proveedor)
admin.site.register(ProveedorTelefonos)
