from django.contrib import admin
from django.urls import path
from .views import ListaEstudiantes, DetalleEstudiantes, ActualizarEstudiantes, EliminarEstudiantes, CrearEstudiantes

urlpatterns = [
    path('', ListaEstudiantes.as_view(), name='lista'),
    path('estudiante/<pk>', DetalleEstudiantes.as_view(), name='detalle'),
    path('agregar/', CrearEstudiantes.as_view(), name='agregar'),
    path('eliminar/<pk>', EliminarEstudiantes.as_view(), name='eliminar'),
    path('actualizar/<pk>', ActualizarEstudiantes.as_view(), name='actualizar'),
]
