from django.db import models

class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.Charfield(max_length=9)
# Create your models here.
