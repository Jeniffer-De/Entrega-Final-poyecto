from django.db import models

class datos(models.Model):
    nombre= models.CharField(max_length=50)
    Cedula= models.FloatField()
    cargo= models.CharField(max_length=50)
    Fecha_inicio= models.FloatField()
    Salario= models.FloatField()
    Tipo_de_contrato= models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    creation_date = models.DateField(auto_now_add=True, null=True, blank=True)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name= "dato"
        verbose_name_plural = "datos"
