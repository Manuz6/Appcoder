from django import forms

class CursoFormulario(forms.Form):
    curso = forms.CharField()
    comision = forms.IntegerField()
    
class BuscaCursoForm(forms.Form):
    curso = forms.CharField()