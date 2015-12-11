from django.contrib import admin

from SistemaDeControlPatrimonial.app.CatalogoBienes.models import Grupo
from SistemaDeControlPatrimonial.app.CatalogoBienes.models import Clase
from SistemaDeControlPatrimonial.app.CatalogoBienes.models import CatalogoBien

admin.site.register(Grupo)
admin.site.register(Clase)
admin.site.register(CatalogoBien)
