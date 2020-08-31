from django.db import models


# Create your models here.


class Matricula(models.Model):
    id = models.CharField(primary_key=True, blank=False, max_length=100)
    id_estudiante = models.ForeignKey('estudiante.Estudiante', on_delete=models.CASCADE)
    codigo_curso = models.ForeignKey('curso.Curso', on_delete=models.CASCADE)
    fecha_matricula = models.DateField()

    def __str__(self):
        return self.id
