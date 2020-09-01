from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from .models import Curso
from django.urls import reverse_lazy


# Create your views here.

class ListaCursos(ListView):
    model = Curso
    template_name = 'Apps/Universidad/Cursos/listado_cursos.html'
    context_object_name = 'Cursos'


class CrearCursos(CreateView):
    model = Curso
    template_name = 'Apps/Universidad/Cursos/agregar_curso.html'
    fields = '__all__'
    success_url = reverse_lazy('Lista-cursos')


class EliminarCursos(DeleteView):
    model = Curso
    template_name = 'Apps/Universidad/Cursos/eliminar_curso.html'
    success_url = reverse_lazy('Lista-cursos')


class ActualizarCursos(UpdateView):
    model = Curso
    template_name = 'Apps/Universidad/Cursos/actualizar_curso.html'
    fields = '__all__'
    success_url = reverse_lazy('Lista-cursos')


class DetalleCurso(DetailView):
    model = Curso
    template_name = 'Apps/Universidad/Cursos/detalle_curso.html'
    context_object_name = 'Curso'
