from django.db import models

# Create your models here.
class institucion(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)