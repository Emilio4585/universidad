from django.db import models


# Create your models here.


class Curso(models.Model):
    codigo = models.CharField(primary_key=True, blank=False, max_length=100)
    nombre = models.CharField(blank=True, max_length=100)
    creditos = models.PositiveSmallIntegerField()
    docente = models.CharField(blank=True, max_length=100)

    def __str__(self):
        return self.nombre
