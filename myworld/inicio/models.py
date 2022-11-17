from django.db import models

# Create your models here.
class usuarios(models.Model):
    primer_nombre = models.CharField(max_length=255)
    segundo_nombre = models.CharField(max_length=255)
    apellidos = models.CharField(max_length=255)
    edad = models.IntegerField()