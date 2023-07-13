from django.db import models

# Create your models here.

class Paquete(models.Model):
    id=models.CharField(primary_key=True,max_length=6)
    nombre=models.CharField(max_length=50)
    precio=models.PositiveIntegerField()
    imagen=models.ImageField(upload_to="paquetes", null=True)

    def __str__(self):
        texto = "{0}"
        return texto.format(self.nombre)
