from django.contrib import admin
from django.urls import path
from .views import ListaEstudiantes, DetalleEstudiantes, ActualizarEstudiantes, EliminarEstudiantes, CrearEstudiantes
urlpatterns = [
    path('', ListaEstudiantes.as_view(), name='Lista-estudiante'),
    path('estudiante/<pk>', DetalleEstudiantes.as_view(), name='detalle-estudiante'),
    path('agregar/', CrearEstudiantes.as_view(), name='agregar-estudiante'),
    path('eliminar/<pk>', EliminarEstudiantes.as_view(), name='elimina-estudiante'),
    path('actualizar/<pk>', ActualizarEstudiantes.as_view(), name='actualiza-estudiante'),
]