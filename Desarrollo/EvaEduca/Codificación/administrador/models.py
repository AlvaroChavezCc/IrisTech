from django.db import models
from profesor.models import profesor
from superadmin.models import institucion

# Create your models here.
class administrador(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    usuario = models.CharField(max_length=50)
    contrasena = models.CharField(max_length=100)
    id_inst_ed = models.OneToOneField(institucion, on_delete=models.CASCADE)

class curso(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    id_profesor = models.ForeignKey(profesor, on_delete=models.CASCADE)
    id_inst_ed = models.ForeignKey(institucion, on_delete=models.CASCADE)

class tareas(models.Model):
    id_curso = models.ForeignKey(curso, on_delete=models.CASCADE)
    tema = models.CharField(max_length=100)
    descripcion = models.TextField()
    rubrica = models.FileField(upload_to='rubricas/')
    archivo = models.FileField(upload_to='archivos/')