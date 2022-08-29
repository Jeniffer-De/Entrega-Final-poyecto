from multiprocessing import context
from django.shortcuts import render


def inicio(request):
    return render(request, "registro.html", context={})
