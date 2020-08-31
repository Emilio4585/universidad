from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from django.urls import reverse_lazy
from .models import Estudiante


# Create your views here.

class ListaEstudiantes(ListView):
    model = Estudiante
    template_name = 'universidad/Estudiantes/listado_Estudiante.html'
    context_object_name = 'Estudiantes'


class CrearEstudiantes(CreateView):
    model = Estudiante
    template_name = 'universidad/Estudiantes/agregar_Estudiante.html'
    fields = '__all__'
    success_url = reverse_lazy('Lista-estudiante')


class EliminarEstudiantes(DeleteView):
    model = Estudiante
    template_name = 'universidad/Estudiantes/eliminar_Estudiante.html'
    success_url = reverse_lazy('Lista-estudiante')


class ActualizarEstudiantes(UpdateView):
    model = Estudiante
    template_name = 'universidad/Estudiantes/actualizar_Estudiante.html'
    fields = '__all__'
    success_url = reverse_lazy('Lista-estudiante')


class DetalleEstudiantes(DetailView):
    model = Estudiante
    template_name = 'universidad/Estudiantes/detalle_Estudiante.html'
    context_object_name = 'Estudiante'
