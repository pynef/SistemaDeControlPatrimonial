from django.contrib import admin

from SistemaDeControlPatrimonial.app.Bienes.models import TipoMedida
from SistemaDeControlPatrimonial.app.Bienes.models import TipoAlmacen
from SistemaDeControlPatrimonial.app.Bienes.models import Almacen
from SistemaDeControlPatrimonial.app.Bienes.models import Inventario
from SistemaDeControlPatrimonial.app.Bienes.models import AltaBien
from SistemaDeControlPatrimonial.app.Bienes.models import DisposicionBien
from SistemaDeControlPatrimonial.app.Bienes.models import AsignacionBien
from SistemaDeControlPatrimonial.app.Bienes.models import TrasladoBien


admin.site.register(TipoMedida)
admin.site.register(TipoAlmacen)
admin.site.register(Almacen)
admin.site.register(Inventario)
admin.site.register(AltaBien)
admin.site.register(DisposicionBien)
admin.site.register(AsignacionBien)
admin.site.register(TrasladoBien)

