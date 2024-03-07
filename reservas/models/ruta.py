from django.db import models

class Ruta(models.Model):
    lugar = models.CharField(null=False, max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.lugar