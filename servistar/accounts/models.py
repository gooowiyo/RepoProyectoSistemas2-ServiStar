from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    ROLES = (
        ('administracion', 'Administración'),
        ('asesor', 'Asesor de Servicio'),
        ('mecanico', 'Mecánica'),
        ('bodega', 'Bodega'),
        ('calidad', 'Control de Calidad'),
    )
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rol = models.CharField(max_length=20, choices=ROLES)
    
    def __str__(self):
        return f"{self.user.username} - {self.rol}"
