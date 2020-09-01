from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('carreras/', include('Apps.College-Crud.carrera.urls', namespace='carreras')),
    path('cursos/', include('Apps.College-Crud.curso.urls', namespace='cursos')),
    path('estudiantes/', include('Apps.College-Crud.estudiante.urls', namespace='estudiantes')),
    path('matriculas/', include('Apps.College-Crud.matricula.urls', namespace='matriculas')),
]
