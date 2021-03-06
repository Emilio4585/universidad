from django.db import models


# Create your models here.

class Estudiante(models.Model):
    dni = models.CharField(primary_key=True, blank=False, max_length=50)
    nombres = models.CharField(blank=False, max_length=50)
    apellidoPaterno = models.CharField(blank=True, max_length=50)
    apellidoMaterno = models.CharField(blank=True, max_length=50)
    fechaNacimiento = models.DateField(blank=True)
    sexos = [
        ('F', 'Femenino'), ('M', 'Masculino')
    ]
    sexo = models.CharField(blank=True, max_length=20, choices=sexos, default='F')
    vigencia = models.BooleanField(default=True)
    codigoCarrera = models.ForeignKey('carrera.Carrera', models.CASCADE, blank=False)

    def __str__(self):
        return self.nombres

    def nombreCompleto(self):
        txt = f'{self.nombres} {self.apellidoPaterno} {self.apellidoMaterno}'
        return txt