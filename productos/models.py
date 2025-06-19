from django.utils import timezone
from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()

    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    creado_en = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nombre
