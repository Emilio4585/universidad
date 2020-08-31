from django.db import models
from django.urls import reverse_lazy
# Create your models here.


class Carrera(models.Model):
    codigo = models.CharField(primary_key=True, blank=False, max_length=100)
    nombre = models.CharField(blank=True, max_length=100)
    duracion = models.PositiveSmallIntegerField(default=5)

    def get_absolute_url(self):
        return reverse_lazy('Lista-carrera')

    def __str__(self):
        return self.nombre

