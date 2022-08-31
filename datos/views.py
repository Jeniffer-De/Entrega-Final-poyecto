from multiprocessing import context
from django.shortcuts import render
from datos.models import datos

# Pagina Cartas laborales.

def create_datos(request):
    cartas_laborales = datos.objects.create(
          nombre= "Ana Carvajal",
          Cedula= "1027863",
          cargo= "lider",
          Fecha_inicio= "2204021",
          Salario= "2000000",
          Tipo_de_contrato= "Indefinido"
         )
    context = {
        "cartas_laborales" : cartas_laborales
    }
    return render(request, "cartas_laborales.html", context=context)

