from django.db import models
from usuarios.models import Usuario
from . import ruta, viajero

class Pasaje(models.Model):
    origen = models.ForeignKey(ruta.Ruta, null=False, on_delete=models.CASCADE, related_name='origenes')
    destino = models.ForeignKey(ruta.Ruta, null=False, on_delete=models.CASCADE, related_name='destinos')
    precio = models.DecimalField(null=False, decimal_places=2, max_digits=10)
    capacidad = models.IntegerField(null=False)
    fecha = models.DateTimeField(null=True)
    transporte = models.CharField(null=False, max_length=20, choices={
        "AV": "Avión",
        "TR": "Tren",
        "BU": "Omnibús",
    })
    
    def __repr__(self):
        return f'{self.origen} - {self.destino} {self.fecha}'
    
    def __str__(self):
        return f'{self.origen} - {self.destino} {self.fecha}'

    def asientos(self):
        ocupados = Viaje.objects.filter(pasaje=self).count()
        return self.capacidad - ocupados

    def tipo(self):
        tipos = {
            "AV": "Avión",
            "TR": "Tren",
            "BU": "Omnibús",
        }
        return tipos[self.transporte]
    
class Viaje(models.Model):
    pasaje = models.ForeignKey(Pasaje, null=False, on_delete=models.CASCADE)
    viajero = models.ForeignKey(viajero.Viajero, null=False, on_delete=models.CASCADE)
    user = models.ForeignKey(Usuario, null=False, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    # estado = models.CharField(null=False, max_length=20, choices={
    #     "A": "Activa",
    #     "R": "Realizada",
    #     "C": "Cancelada",
    # })