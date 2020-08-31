from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from .models import Matricula
from django.urls import reverse_lazy


# Create your views here.

class ListaMatriculas(ListView):
    model = Matricula
    template_name = 'universidad/Matriculas/listado_Matriculas.html'
    context_object_name = 'Matriculas'


class CrearMatriculas(CreateView):
    model = Matricula
    template_name = 'universidad/Matriculas/agregar_Matricula.html'
    fields = '__all__'
    success_url = reverse_lazy('Lista-matricula')


class EliminarMatriculas(DeleteView):
    model = Matricula
    template_name = 'universidad/Matriculas/eliminar_Matricula.html'
    success_url = reverse_lazy('Lista-matricula')


class ActualizarMatricula(UpdateView):
    model = Matricula
    template_name = 'universidad/Matriculas/actualizar_Matricula.html'
    fields = '__all__'
    success_url = reverse_lazy('Lista-matricula')


class DetalleMatriculas(DetailView):
    model = Matricula
    template_name = 'universidad/Matriculas/detalle_Matricula.html'
    context_object_name = 'Matricula'
