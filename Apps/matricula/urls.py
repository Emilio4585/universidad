from django.contrib import admin
from django.urls import path
from .views import ListaMatriculas, DetalleMatriculas, CrearMatriculas, EliminarMatriculas, ActualizarMatricula
urlpatterns = [
    path('', ListaMatriculas.as_view(), name='Lista-matricula'),
    path('matricula/<pk>', DetalleMatriculas.as_view(), name='detalle-matricula'),
    path('agregar/', CrearMatriculas.as_view(), name='agregar-matricula'),
    path('eliminar/<pk>', EliminarMatriculas.as_view(), name='elimina-matricula'),
    path('actualizar/<pk>', ActualizarMatricula.as_view(), name='actualiza-matricula'),
]