from django.shortcuts import render
from acerca_de.models import informacion

def crear_informacion(request):
    nuev_text = informacion.objects.create(
        title = "PORTAL EMPLEADOS",
        texto_1= "Puede generar su certificado laboral",
        texto_2= "Puede soliictar licencias",
        texto_3= "Conozca mas de la empresa") 
