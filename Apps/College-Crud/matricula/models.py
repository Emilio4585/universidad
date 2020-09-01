from django.db import models


# Create your models here.


class Matricula(models.Model):
    id = models.AutoField(primary_key=True)
    id_estudiante = models.ForeignKey('estudiante.Estudiante', null=False, blank=False, on_delete=models.CASCADE)
    codigo_curso = models.ForeignKey('curso.Curso', null=False, blank=False, on_delete=models.CASCADE)
    fecha_matricula = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id
