from django.db import models
from django.utils import timezone

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(default="Sin descripción")
    precio = models.FloatField()
    stock = models.IntegerField()
    disponible = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(default=timezone.now)
    categoria = models.CharField(max_length=50, default="General")

    def __str__(self):
        return self.nombre
