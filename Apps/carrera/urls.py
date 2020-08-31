from django.contrib import admin
from django.urls import path
from .views import ListaCarreras, CrearCarreras, EliminarCarreras, ActualizarCarreras, DetalleCarrera

urlpatterns = [
    path('', ListaCarreras.as_view(), name='Lista-carrera'),
    path('carrera/<pk>', DetalleCarrera.as_view(), name='detalle-carrera'),
    path('agregar/', CrearCarreras.as_view(), name='agregar-carrera'),
    path('eliminar/<pk>', EliminarCarreras.as_view(), name='elimina-carrera'),
    path('actualizar/<pk>', ActualizarCarreras.as_view(), name='actualiza-carrera'),
]
