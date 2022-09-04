from multiprocessing import context
from django.shortcuts import render
from acerca_de.models import Informacion

#Pagina acerca de:
def create_informacion(request):
    nueva_informacion = Informacion.objects.create(
         title = "PORTAL EMPLEADOS",
         texto_1= "Puede generar su certificado laboral.",
         texto_2= "Puede solicitar licencias",
         texto_3= "Conozca mas de la empresa"
         ) 
    context = {
        "nueva_informacion":nueva_informacion
    }
    return render(request, "nueva_informacion.html", context=context)
