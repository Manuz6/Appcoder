from django.urls import path

from appcoder.views import inicio, cursos, estudiantes, profesores, entregables

urlpatterns = [
    path('pagina-inicio', inicio),
    path('pagina-cursos', cursos),
    path('pagina-estudiantes', estudiantes),
    path('pagina-profesores', profesores),
    path('pagina-entregables', entregables),    
]


