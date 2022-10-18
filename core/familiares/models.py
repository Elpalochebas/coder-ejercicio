from django.db import models

# Create your models here.

class Familiar( models.Model ):

    nombre = models.CharField(max_length=20)
    apellido_paterno = models.CharField(max_length=20)
    apellido_materno = models.CharField(max_length=20)
    edad = models.IntegerField()

    def __str__(self):
        return f'{ self.nombre } mi familiar'
