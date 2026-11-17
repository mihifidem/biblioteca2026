from django.db import models


class Genero(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


    
# Create your models here.
class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=200)
    anio = models.IntegerField()
    disponible = models.BooleanField(default=True)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.titulo