from multiprocessing import context
from django.shortcuts import render
from licencias.models import licencias

# Pagina Licencias y permisos.

def create_licencias(request):
    licencias_y_permisos = licencias.objects.create(
          nombre= "Ana Carvajal",
          Cedula= "1027863",
          cargo= "lider",
          Fecha_Permiso= "2204021",
          Total_horas=  "2",
          Motivo_Permiso= "personal"
         )
    context = {
        "licencias_y_permisos" : licencias_y_permisos
    }
    return render(request, "Licencias_y_permisos.html", context=context)

