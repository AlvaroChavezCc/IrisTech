from django.db import models
from superadmin.models import institucion

# Create your models here.
class profesor(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    usuario = models.CharField(max_length=50)
    contrasena = models.CharField(max_length=100)
    id_inst_ed = models.ForeignKey(institucion, on_delete=models.CASCADE)