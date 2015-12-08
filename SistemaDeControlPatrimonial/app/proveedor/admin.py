import socket
from django.contrib import admin


from SistemaDeControlPatrimonial.app.proveedor.models import Proveedor
from SistemaDeControlPatrimonial.app.proveedor.models import ProveedorTelefonos


admin.site.register(Proveedor)
admin.site.register(ProveedorTelefonos)
