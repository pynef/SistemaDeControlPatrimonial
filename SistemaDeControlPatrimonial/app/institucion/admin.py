import socket
from django.contrib import admin
from SistemaDeControlPatrimonial.app.institucion.models import TipoAmbiente
from SistemaDeControlPatrimonial.app.institucion.models import Institucion
from SistemaDeControlPatrimonial.app.institucion.models import Sede
from SistemaDeControlPatrimonial.app.institucion.models import Local
from SistemaDeControlPatrimonial.app.institucion.models import Ambiente



admin.site.register(TipoAmbiente)
admin.site.register(Institucion)
admin.site.register(Sede)
admin.site.register(Local)
admin.site.register(Ambiente)

# class InstitucionAdmin(admin.ModelAdmin):
# 	list_display = ('nombre',
# 					'razon_social',
# 					'direccion_fiscal',
# 					'email',
# 					'ruc',
# 					'user',
# 					'workstation_name',
# 					'workstation_ip',)
# 	exclude = ('user', 'workstation_name', 'workstation_ip',)

# 	def save_model(self, request, obj, form, change):
# 		obj.user = request.user
# 		obj.workstation_name = socket.gethostname()
# 		obj.workstation_ip = socket.gethostbyname(socket.gethostname())
# 		obj.save()

# admin.site.register(Institucion, InstitucionAdmin)
