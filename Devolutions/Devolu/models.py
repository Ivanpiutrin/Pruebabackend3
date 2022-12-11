from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.utils import timezone

"""class Cliente(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, verbose_name='Email')
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(timezone.now)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


    def __str__(self):
        return self.email"""

class AdminUser(AbstractUser):
    rut = models.CharField(max_length=10)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    celular = models.PositiveIntegerField(blank=True, null=True)


# Create your models here.
class DCliente(models.Model):
    rut = models.CharField(max_length=10)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    celular = models.PositiveIntegerField()
    
    
class Devolucion(models.Model):
    cliente = models.ForeignKey(DCliente, on_delete=models.CASCADE)
    cantidad = models.CharField(max_length=100)
    producto = models.CharField(max_length=100)
    codigo = models.CharField(max_length=100)
    nombre_vendedor = models.CharField(max_length=100)
    distribuidor = models.CharField(max_length=100)
    comentario = models.CharField(max_length=100)