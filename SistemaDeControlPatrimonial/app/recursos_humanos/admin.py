import socket
from django.contrib import admin

from SistemaDeControlPatrimonial.app.recursos_humanos.models import Persona
from SistemaDeControlPatrimonial.app.recursos_humanos.models import PersonaTelefono
from SistemaDeControlPatrimonial.app.recursos_humanos.models import Trabajador
from SistemaDeControlPatrimonial.app.recursos_humanos.models import Area
from SistemaDeControlPatrimonial.app.recursos_humanos.models import Puesto
from SistemaDeControlPatrimonial.app.recursos_humanos.models import TrabajadorPuesto


admin.site.register(Persona)
admin.site.register(PersonaTelefono)
admin.site.register(Trabajador)
admin.site.register(Area)
admin.site.register(Puesto)
admin.site.register(TrabajadorPuesto)
