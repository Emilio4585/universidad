from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from .models import Carrera
from django.urls import reverse_lazy


# Create your views here.

class ListaCarreras(ListView):
    model = Carrera
    template_name = 'universidad/Carreras/listado_carreras.html'
    context_object_name = 'Carreras'


class CrearCarreras(CreateView):
    model = Carrera
    template_name = 'universidad/Carreras/agregar_carreras.html'
    fields = '__all__'
    success_url = reverse_lazy('Lista-carrera')

class EliminarCarreras(DeleteView):
    model = Carrera
    template_name = 'universidad/Carreras/eliminar_carreras.html'
    success_url = reverse_lazy('Lista-carrera')


class ActualizarCarreras(UpdateView):
    model = Carrera
    template_name = 'universidad/Carreras/actualizar_carrera.html'
    fields = '__all__'
    success_url = reverse_lazy('Lista-carrera')


class DetalleCarrera(DetailView):
    model = Carrera
    template_name = 'universidad/Carreras/detalle_carrera.html'
    context_object_name = 'Carrera'
