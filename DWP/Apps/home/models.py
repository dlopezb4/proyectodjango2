from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    direccion = models.CharField(max_length=200)
    email = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    tipo = models.ForeignKey(
        'TipoCliente',
        on_delete= models.CASCADE,
        default=1
    )
    creacion = models.DateField(auto_now_add=True)
    actualizacion = models.DateField(auto_now_add=True)

    def __srt__(self):
        return '%s %s' % (self.nombre, self.apellido)

class TipoCliente(models.Model):
    tipo = models.CharField(max_length=50)
    creacion = models.DateField(auto_now_add=True)
    actualizacion = models.DateField(auto_now_add=True)

    def __srt__(self):
        return '%s %s' % (self.nombre, self.apellido)

