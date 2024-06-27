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

    def __str__(self):
        return self.nombre


# Modelo para representar los exámenes disponibles para descargar
class Examen(models.Model):
    nombre = models.CharField(max_length=100)
    archivo = models.FileField(upload_to='examenes/')

    def __str__(self):
        return self.nombre

# Modelo para representar las respuestas de los alumnos a los exámenes
class Respuesta(models.Model):
    alumno = models.ForeignKey(User, on_delete=models.CASCADE)
    tareas = models.ForeignKey(tareas, on_delete=models.CASCADE)  # Asociar la respuesta a la tarea creada por el administrador
    archivo_respuesta = models.FileField(upload_to='respuestas/')

    def __str__(self):
        return f'Respuesta de {self.alumno.username} para la tarea {self.tareas.id}'
    
# Modelo para evaluación en la base de datos
class evaluacion(models.Model):
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    id_alumno = models.ForeignKey('alumno', on_delete=models.CASCADE)
    id_curso = models.ForeignKey(curso, on_delete=models.CASCADE)

    def __str__(self):
        return f"Evaluación de {self.id_alumno.nombre} en {self.id_curso.nombre}"
