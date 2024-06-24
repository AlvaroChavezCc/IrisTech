from django.db import models

from administrador.models import curso
from profesor.models import profesor
from superadmin.models import institucion

# Create your models here.
class evaluacion(models.Model):
    file = models.FileField(upload_to='uploads/') # Esta parte todavía falta analizar, pero algo así sería para subir
    uploaded_at = models.DateTimeField(auto_now_add=True)
    id_curso = models.ForeignKey(curso, on_delete=models.CASCADE)
    id_profesor = models.ForeignKey(profesor, on_delete=models.CASCADE)

class alumno(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    usuario = models.CharField(max_length=50)
    contrasena = models.CharField(max_length=100)
    id_curso = models.ForeignKey(curso, on_delete=models.CASCADE)
    id_inst_ed = models.ForeignKey(institucion, on_delete=models.CASCADE)