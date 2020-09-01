from django.contrib import admin
from django.urls import path
from .views import ListaMatriculas, DetalleMatriculas, CrearMatriculas, EliminarMatriculas, ActualizarMatricula

urlpatterns = [
    path('', ListaMatriculas.as_view(), name='lista'),
    path('matricula/<pk>', DetalleMatriculas.as_view(), name='detalle'),
    path('agregar/', CrearMatriculas.as_view(), name='agregar'),
    path('eliminar/<pk>', EliminarMatriculas.as_view(), name='eliminar'),
    path('actualizar/<pk>', ActualizarMatricula.as_view(), name='actualizar'),
]
