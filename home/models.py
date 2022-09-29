from django.db import models

# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    edad = models.IntegerField()    
    fecha_nacimiento = models.DateField(null=True)
    
class Familiar(models.Model):
    nombre = models.CharField(max_length=30)
    parentezco = models.CharField(max_length=30)
    edad = models.IntegerField()    
    fecha_nacimiento = models.DateField(null=True)