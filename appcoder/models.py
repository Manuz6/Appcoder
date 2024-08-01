from django.db import models

# Create your models here.

class Curso(models.Model):
    nombre = models.CharField(max_length=30)
    comision = models.IntegerField()
    def __str__(self):
         return f"{self.comision}, {self.nombre}"
    
class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    def __str__(self):
        return f"{self.apellido}, {self.nombre}"

    
class Profesor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    profesion = models.CharField(max_length=40)
    def __str__(self):
        return f"{self.apellido}, {self.nombre}"

    
class Entregable(models.Model):
    nombre = models.CharField(max_length=30)
    fecha_de_entrega = models.DateField()
    entregado = models.BooleanField()
    def __str__(self):
        texto_entregado = "Entregado" if self.entregado else "No entregado"
        return f"Entregable: {self.nombre} | Fecha: {self.fecha_de_entrega} | Estado: {texto_entregado}"

