from django.db import models

# Create your models here.
from unittest.util import _MAX_LENGTH
from django.contrib.auth.models import User

class Mensajes(models.Model):
    emisor_mensaje = models.CharField(max_length=50)
    receptor_mensaje= models.CharField(max_length=50)
    fecha_mensaje= models.DateField()
    texto_mensaje=models.TextField( null=True, blank=True)
    leido_mensaje= models.BooleanField(default=False)
    imagen_mensaje=models.ImageField(upload_to='mensajes', null=True, blank=True)
    def __str__(self):
        if self.receptor is None:
            return self.fecha_mensaje+" De: "+self.emisor_mensaje+" A: Todos"
        else:
             return self.fecha_mensaje+" De: "+self.emisor_mensaje+" A: "+self.receptor_mensaje