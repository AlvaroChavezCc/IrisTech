from django.db import models

from administrador.models import curso, tareas
from profesor.models import profesor
from superadmin.models import institucion

# Create your models here.

class alumno(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    usuario = models.CharField(max_length=50)
    contrasena = models.CharField(max_length=100)
    id_curso = models.ManyToManyField(curso, through='AlumnoCurso')
    id_inst_ed = models.ForeignKey(institucion, on_delete=models.CASCADE)

class evaluacion(models.Model):
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    id_curso = models.ForeignKey(curso, on_delete=models.CASCADE)
    id_alumno = models.ForeignKey(alumno, on_delete=models.CASCADE)
    id_tarea = models.ForeignKey(tareas, on_delete=models.CASCADE, null=True)
    nota = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    respuesta = models.TextField(null=True, blank=True)

class reclamo(models.Model):
    id_evaluacion = models.ForeignKey(evaluacion, on_delete=models.CASCADE)
    id_alumno = models.ForeignKey(alumno, on_delete=models.CASCADE)
    descripcion = models.TextField(null=True, blank=True)
    respuesta = models.TextField(null=True, blank=True)
    estado = models.BooleanField(default=True)

class alumnoCurso(models.Model):
    alumno = models.ForeignKey(alumno, on_delete=models.CASCADE)
    curso = models.ForeignKey(curso, on_delete=models.CASCADE)
    grado = models.CharField(max_length=50)
    nivel = models.CharField(max_length=50)
    seccion = models.CharField(max_length=50)