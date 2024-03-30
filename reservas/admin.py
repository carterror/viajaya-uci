from django.contrib import admin
from reservas.models import agencia, pasaje, ruta, viajero
# Register your models here.
admin.site.register(ruta.Ruta)
admin.site.register(viajero.Viajero)
admin.site.register(pasaje.Pasaje)
admin.site.register(pasaje.Viaje)
admin.site.register(agencia.Agencia)
