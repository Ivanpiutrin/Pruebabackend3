from django.db import models

# Create your models here.
class DCliente(models.Model):
    rut = models.CharField(max_length=10)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    celular = models.PositiveIntegerField()
    cantidad = models.CharField(max_length=100)
    producto = models.CharField(max_length=100)
    codigo = models.CharField(max_length=100)
    nombrevendedor = models.CharField(max_length=100)
    distribuidor = models.CharField(max_length=100)
    comentario = models.CharField(max_length=100)
    