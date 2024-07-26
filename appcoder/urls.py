from django.urls import path

from appcoder.views import inicio, cursos, estudiantes, profesores, entregables, curso_formulario

urlpatterns = [
    path('pagina-inicio', inicio, name="inicio"),
    path('pagina-cursos', cursos, name="cursos"),
    path('pagina-estudiantes', estudiantes, name="estudiantes"),
    path('pagina-profesores', profesores, name="profesores"),
    path('pagina-entregables', entregables, name="entregables"),
    path('pagina-formulario', curso_formulario, name="curso_formulario"),    
]


