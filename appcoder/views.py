from django.shortcuts import render
from django.http import HttpResponse
from appcoder.models import Curso
from appcoder.forms import CursoFormulario
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


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
        
        curso = Curso(nombre=request.POST['curso'], comision=request.POST['comision'])
        curso.save()
        
        return render(request, "appcoder/inicio.html")
    
    return render (request, "appcoder/curso_formulario.html")



def form_con_api(request):
    if request.method == "POST":
        mi_formulario = CursoFormulario(request.POST)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            
            curso = Curso(nombre=informacion["curso"], comision=informacion["comision"])
            curso.save()
            
            return render(request, "appcoder/inicio.html")
    else:
        mi_formulario = CursoFormulario()
    return render(request, "appcoder/form_con_api.html", {"mi_formulario": mi_formulario})    

def buscar_form_con_api(request):
    if request.method == "POST":
        miFormulario = BuscaCursoForm(request.POST) # Aqui me llega la informacion del html

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            
            cursos = Curso.objects.filter(nombre__icontains=informacion["curso"])

            return render(request, "AppCoder/resultados_buscar_form.html", {"cursos": cursos})
    else:
        miFormulario = BuscaCursoForm()

    return render(request, "AppCoder/buscar_form_con_api.html", {"miFormulario": miFormulario})

class CursoListview(ListView):
    model = Curso
    context_object_name = "cursos"
    template_name = "appcoder/listar.html"
    
class CursoCreateView(CreateView):
    model = Curso
    template_name = "appcoder/create.html"
    success_url = reverse_lazy("ListarCursos")
    fields = ["nombre", "comision"]
    
class CursoUpdateView(UpdateView):
    model = Curso
    template_name = "appcoder/actualizar.html"
    fields = ["nombre", "comision"]
    success_url = reverse_lazy("ListarCursos")
    
class CursoDeleteView(DeleteView):
    model = Curso
    template_name = "appcoder/borrar.html"
    success_url = reverse_lazy("ListarCursos")