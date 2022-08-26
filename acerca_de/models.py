from turtle import title
from django.db import models

class informacion (models.Model):
    title= models.CharField(max_length=50)
    texto_1= models.CharField(max_length=500)
    texto_2= models.CharField(max_length=500)
    texto_3= models.CharField(max_length=500)
    
