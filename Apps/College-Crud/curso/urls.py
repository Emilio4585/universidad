from django.contrib import admin
from django.urls import path
from .views import CrearCursos, DetalleCurso, ListaCursos, ActualizarCursos, EliminarCursos
app_name = 'cursos'
urlpatterns = [
    path('', ListaCursos.as_view(), name='lista'),
    path('curso/<pk>', DetalleCurso.as_view(), name='detalle'),
    path('agregar/', CrearCursos.as_view(), name='agregar'),
    path('eliminar/<pk>', EliminarCursos.as_view(), name='eliminar'),
    path('actualizar/<pk>', ActualizarCursos.as_view(), name='actualizar'),
path('buscar/', ActualizarCursos.as_view(), name='buscar'),
]
