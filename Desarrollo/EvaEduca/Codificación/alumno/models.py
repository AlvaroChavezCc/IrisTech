from django.db import models
from django.contrib.auth.models import User
from administrador.models import tareas  # Asegúrate de importar correctamente el modelo tareas desde tu aplicación
from administrador.models import curso
from superadmin.models import institucion

# Modelo para representar a los alumnos
class alumno(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    usuario = models.CharField(max_length=50)
    contrasena = models.CharField(max_length=100)
    id_curso = models.ForeignKey(curso, on_delete=models.CASCADE)
    id_inst_ed = models.ForeignKey(institucion, on_delete=models.CASCADE)



    
# Modelo para evaluación en la base de datos
class evaluacion(models.Model):
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    id_curso = models.ForeignKey(curso, on_delete=models.CASCADE)
    id_alumno = models.ForeignKey(alumno, on_delete=models.CASCADE)
    id_tarea = models.ForeignKey(tareas, on_delete=models.CASCADE, null=True)
