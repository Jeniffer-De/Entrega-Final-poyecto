from django.shortcuts import render

# Pagina Cartas laborales.

def datos_personal(request):
    return render(request, "cartas_laborales.html", context={})
