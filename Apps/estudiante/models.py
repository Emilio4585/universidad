from django.db import models


# Create your models here.

class Estudiante(models.Model):
    dni = models.CharField(primary_key=True, blank=False, max_length=50)
    apellidoPaterno = models.CharField(blank=True, max_length=50)
    apellidoMaterno = models.CharField(blank=True, max_length=50)
    nombres = models.CharField(blank=False, max_length=50)
    fechaNacimiento = models.DateField(blank=True)
    sexos = [
        ('F', 'Femenino'), ('M', 'Masculino')
    ]
    sexo = models.CharField(blank=True, max_length=20, choices=sexos, default='F')
    vigencia = models.IntegerField()
    codigoCarrera = models.ForeignKey('carrera.Carrera', models.CASCADE, blank=True)

    def __str__(self):
        return self.nombres
