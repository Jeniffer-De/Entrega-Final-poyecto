from multiprocessing import context
from django.shortcuts import render
from licencias.models import licencias

from django.contrib.auth.decorators import login_required


# Pagina Licencias y permisos.

@login_required
def create_licencias(request):
    licencias_y_permisos = licencias.objects.create(
          nombre= "Ana Carvajal",
          Cedula= "1027863",
          cargo= "Lider",
          Fecha_Permiso= "2204021",
          Total_horas=  "2",
          Motivo_Permiso= "Por calamidad domestica"
         )
    context = {
        "licencias_y_permisos" : licencias_y_permisos
    }
    return render(request, "Licencias_y_permisos.html", context=context)

