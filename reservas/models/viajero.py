from django.db import models
from usuarios.models import Usuario

class Viajero(models.Model):
    nombre = models.CharField(max_length=100, null=False)
    ci = models.CharField(max_length=11, null=False)
    user = models.ForeignKey(Usuario, null=False, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)