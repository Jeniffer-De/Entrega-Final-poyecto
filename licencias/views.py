from django.shortcuts import render

# Pagina Licencias y permisos.

def licencias(request):
    return render(request, "Licencias_y_permisos.html", context={})