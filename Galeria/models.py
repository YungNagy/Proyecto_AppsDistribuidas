from django.db import models

class Producto(models.Model):
    nombre=models.CharField(max_length=64)
    categoria=models.CharField(max_length=32,default="Ninguna")
    precio=models.IntegerField()
    imagen=models.CharField(max_length=200,default="image not found")

    def __str__(self):
        return f'{self.nombre} -> {self.precio}'