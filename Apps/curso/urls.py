from django.contrib import admin
from django.urls import path
from .views import CrearCursos, DetalleCurso, ListaCursos, ActualizarCursos, EliminarCursos
urlpatterns = [
    path('', ListaCursos.as_view(), name='Lista-cursos'),
    path('curso/<pk>', DetalleCurso.as_view(), name='detalle-curso'),
    path('agregar/', CrearCursos.as_view(), name='agregar-curso'),
    path('eliminar/<pk>', EliminarCursos.as_view(), name='elimina-curso'),
    path('actualizar/<pk>', ActualizarCursos.as_view(), name='actualiza-curso'),
]