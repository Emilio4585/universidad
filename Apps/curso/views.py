from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from .models import Curso
from django.urls import reverse_lazy


# Create your views here.

class ListaCursos(ListView):
    model = Curso
    template_name = 'universidad/Cursos/listado_cursos.html'
    context_object_name = 'Cursos'


class CrearCursos(CreateView):
    model = Curso
    template_name = 'universidad/Cursos/listado_cursos.html'
    fields = '__all__'


class EliminarCursos(DeleteView):
    model = Curso
    template_name = 'universidad/Cursos/listado_cursos.html'
    success_url = reverse_lazy('Lista-cursos')


class ActualizarCursos(UpdateView):
    model = Curso
    template_name = 'universidad/Cursos/listado_cursos.html'
    fields = '__all__'
    success_url = reverse_lazy('Lista-cursos')


class DetalleCurso(DetailView):
    model = Curso
    template_name = 'universidad/Cursos/listado_cursos.html'
    context_object_name = 'Curso'
