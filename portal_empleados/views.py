from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render

def inicio_1(request):
    return HttpResponse("Hola inicia sesion") 


def inicio(request):
    return render(request, "registro.html", context={})


def index(request):
    return render(request, "index.html")