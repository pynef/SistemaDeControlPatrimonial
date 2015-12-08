from django.contrib import admin

from SistemaDeControlPatrimonial.app.bienes.models import TipoMedida
from SistemaDeControlPatrimonial.app.bienes.models import TipoAlmacen
from SistemaDeControlPatrimonial.app.bienes.models import Almacen
from SistemaDeControlPatrimonial.app.bienes.models import Inventario
from SistemaDeControlPatrimonial.app.bienes.models import AltaBien
from SistemaDeControlPatrimonial.app.bienes.models import DisposicionBien
from SistemaDeControlPatrimonial.app.bienes.models import AsignacionBien
from SistemaDeControlPatrimonial.app.bienes.models import TrasladoBien


admin.site.register(TipoMedida)
admin.site.register(TipoAlmacen)
admin.site.register(Almacen)
admin.site.register(Inventario)
admin.site.register(AltaBien)
admin.site.register(DisposicionBien)
admin.site.register(AsignacionBien)
admin.site.register(TrasladoBien)

