from django.contrib import admin
from django.urls import path
from .views import ListaCarreras, CrearCarreras, EliminarCarreras, ActualizarCarreras, DetalleCarrera
app_name = 'carreras'

urlpatterns = [
    path('', ListaCarreras.as_view(), name='lista'),
    path('carrera/<pk>', DetalleCarrera.as_view(), name='detalle'),
    path('agregar/', CrearCarreras.as_view(), name='agregar'),
    path('eliminar/<pk>', EliminarCarreras.as_view(), name='eliminar'),
    path('actualizar/<pk>', ActualizarCarreras.as_view(), name='actualizar'),
    path('buscar/', ActualizarCarreras.as_view(), name='buscar'),
]
