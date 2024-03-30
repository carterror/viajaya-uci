from django.db import models


class Agencia(models.Model):
    nombre = models.CharField(max_length=100, null=False)
    provincia = models.CharField(max_length=50, null=False)
    telefono = models.CharField(max_length=12, null=False)
    direccion = models.CharField(max_length=250, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        app_label = 'reservas'