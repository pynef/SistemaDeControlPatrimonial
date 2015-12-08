from django.contrib import admin

from SistemaDeControlPatrimonial.app.catalogo_bienes.models import Grupo
from SistemaDeControlPatrimonial.app.catalogo_bienes.models import Clase
from SistemaDeControlPatrimonial.app.catalogo_bienes.models import CatalogoDeBien

admin.site.register(Grupo)
admin.site.register(Clase)
admin.site.register(CatalogoDeBien)
