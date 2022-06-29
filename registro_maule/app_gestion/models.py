from django.db import models

# Create your models here.
class Vacunado(models.Model):
    rut=models.CharField(max_length=12)
    nombre=models.CharField(max_length=30)
    appaterno=models.CharField(max_length=30)
    apmaterno=models.CharField(max_length=30)
    edad=models.CharField(max_length=2)
    nom_vacuna=models.CharField(max_length=10)
    fecha=models.CharField(max_length=10)