from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from .models import Carrera
from django.urls import reverse_lazy


# Create your views here.

class ListaCarreras(ListView):
    model = Carrera
    template_name = 'Apps/Universidad/Carreras/listado_carreras.html'
    context_object_name = 'Carreras'


class CrearCarreras(CreateView):
    model = Carrera
    template_name = 'Apps/Universidad/Carreras/agregar_carrera.html'
    fields = '__all__'
    success_url = reverse_lazy('carreras:lista')


class EliminarCarreras(DeleteView):
    model = Carrera
    template_name = 'Apps/Universidad/Carreras/eliminar_carrera.html'
    success_url = reverse_lazy('carreras:lista')
    context_object_name = 'Carrera'


class ActualizarCarreras(UpdateView):
    model = Carrera
    template_name = 'Apps/Universidad/Carreras/actualizar_carrera.html'
    fields = '__all__'
    success_url = reverse_lazy('carreras:lista')


class DetalleCarrera(DetailView):
    model = Carrera
    template_name = 'Apps/Universidad/Carreras/detalle_carrera.html'
    context_object_name = 'Carrera'
