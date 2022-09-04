from contextlib import redirect_stderr
from multiprocessing import context
from unicodedata import name
from django.shortcuts import render, redirect
from datos.models import datos
from datos.forms import Formulario_datos

# Pagina Cartas laborales.

def create_datos(request):
    print(request.POST)
    if request.method == "POST":
       form = Formulario_datos(request.POST)
       
       if form.is_valid():
           datos.objects.create(
               nombre = form.cleaned_data["nombre"],
               cedula= form.cleaned_data ["cedula"],
               cargo = form.cleaned_data ["cargo"],
               Fecha_inicio = form.cleaned_data ["Fecha_inicio"],
               Salario = form.cleaned_data ["Salario"],
               Tipo_de_contrato = form.cleaned_data ["Tipo_de_contrato"]
           )
           return redirect ("licencias_y_permisos")
        
    elif request.method == "GET":
        form = Formulario_datos()
        context = {"form":form}
        return render(request,"cartas_laborales.html", context=context)
 
#  def create_datos(request):
#     cartas_laborales = datoscar.objects.create(
#          nombre = "PORTAL EMPLEADOS",
#          Cedula= "Puede generar su certificado laboral.",
#          cargo= "Puede solicitar licencias",
#          Fecha_inicio= "Conozca mas de la empresa",
#          Salario = "1500000"
#          Tipo_de_contrato= "Indefinido"
#          ) 
#     context = {
#         "cartas_laborales":cartas_laborales
#     }
#     return render(request, "cartas_laborales.html", context=context)   
            
def formulario_1(request):
    print(request.method)
    if request.method == "POST" :
        datos.objects.create(name=request.POST["name"]          
        )
    return render (request, "formulario_1.html", context={})            
    