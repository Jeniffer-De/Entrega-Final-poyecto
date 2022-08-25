from django.db import models

class datos(models.Model):
    nombre= models.CharField(max_length=50)
    Cedula= models.FloatField()
    cargo= models.CharField(max_length=50)
    Fecha_inicio= models.FloatField()
    Salario= models.FloatField()
    is_active = models.BooleanField()
