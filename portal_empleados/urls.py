from pathlib import Path
from django.contrib import admin
from django.urls import path, include
from portal_empleados.views import inicio ,inicio_1 , index
from acerca_de.views import create_informacion
from datos.views import create_datos, formulario_1
from licencias.views import create_licencias

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path("",index, name="index"),
    
    path('inicio/',inicio, name='inicio'),
    path('create_informacion/',create_informacion, name='create_informacion'),
    path("create_datos/",create_datos, name="create_datos"),
    path("create_licencias/",create_licencias, name="create_licencias"),
    path("formulario_1/",formulario_1, name= "formulario_1"),
    path("usuarios/", include("usuarios.urls"))
]
