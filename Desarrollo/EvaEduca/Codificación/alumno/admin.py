from django.contrib import admin
from .models import alumno, Examen, Respuesta

# Register your models here.
admin.site.register(alumno)
admin.site.register(Examen)
admin.site.register(Respuesta)

