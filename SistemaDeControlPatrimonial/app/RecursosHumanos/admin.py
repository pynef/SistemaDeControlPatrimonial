import socket
from django.contrib import admin

from SistemaDeControlPatrimonial.app.RecursosHumanos.models import Persona
from SistemaDeControlPatrimonial.app.RecursosHumanos.models import PersonaTelefono
from SistemaDeControlPatrimonial.app.RecursosHumanos.models import Trabajador
from SistemaDeControlPatrimonial.app.RecursosHumanos.models import Area
from SistemaDeControlPatrimonial.app.RecursosHumanos.models import Puesto
from SistemaDeControlPatrimonial.app.RecursosHumanos.models import TrabajadorPuesto


admin.site.register(Persona)
admin.site.register(PersonaTelefono)
admin.site.register(Trabajador)
admin.site.register(Area)
admin.site.register(Puesto)
admin.site.register(TrabajadorPuesto)
