from django.urls import path

from appcoder.views import *

urlpatterns = [
    path('pagina-inicio/', inicio, name="inicio"),
    path('pagina-cursos/', cursos, name="cursos"),
    path('pagina-estudiantes/', estudiantes, name="estudiantes"),
    path('pagina-profesores/', profesores, name="profesores"),
    path('pagina-entregables/', entregables, name="entregables"),
    path('pagina-formulario/', curso_formulario, name="curso_formulario"),
    path('form-con-api/', form_con_api, name="FormConApi"),
    path('listar/', CursoListview.as_view(), name="ListarCursos"),
    path('crear/', CursoCreateView.as_view(), name="CrearCurso"),
    path('update/<pk>/', CursoUpdateView.as_view(), name="ActualizarCurso"),
    path('delete/<pk>/', CursoDeleteView.as_view(), name="DeleteCurso")
]


