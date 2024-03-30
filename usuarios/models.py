from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    # Aquí puedes añadir campos adicionales si son necesarios
    ci = models.CharField(null=False, max_length=11, default='0')
    
    class Meta:
        app_label = 'usuarios'