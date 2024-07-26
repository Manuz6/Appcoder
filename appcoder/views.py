from django.shortcuts import render
from django.http import HttpResponse
from appcoder.models import Curso
from appcoder.forms import CursoFormulario

# Create your views here.

def inicio(request):
    return render(request, "appcoder/inicio.html")

def cursos(request):
    return render(request, "appcoder/cursos.html")

def estudiantes(request):
    return render(request, "appcoder/estudiantes.html")

def profesores(request):
    return render(request, "appcoder/profesores.html")

def entregables(request):
    return render(request, "appcoder/entregables.html")



def curso_formulario(request):
    if request.method == 'POST':
        
        curso = Curso(nombre=request.POST['curso'], camada=request.POST['camada'])
        curso.save()
        
        return render(request, "appcoder/inicio.html")
    
    return render (request, "appcoder/curso_formulario.html")



def form_con_api(request):
    if request.method == "POST":
        mi_formulario = CursoFormulario(request.POST)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            
            curso = Curso(nombre=informacion["curso"], camada=informacion["camada"])
            curso.save()
            
            return render(request, "appcoder/inicio.html")
    else:
        mi_formulario = CursoFormulario()
    return render(request, "appcoder/form_con_api.html", {"mi_formulario": mi_formulario})    
