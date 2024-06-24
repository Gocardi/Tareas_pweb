from django.db import models
from django.urls import reverse

class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    email = models.EmailField()

    def get_absolute_url(self):
        return reverse('personas:detalle', args=[str(self.id)])
# Create your models here.
