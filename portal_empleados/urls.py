from pathlib import Path
from django.contrib import admin
from django.urls import path
from portal_empleados.views import inicio
from acerca_de.views import create_informacion
from datos.views import create_datos
from licencias.views import create_licencias

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/',inicio, name='inicio'),
    path('create_informacion/',create_informacion, name='create_informacion'),
    path("create_datos/",create_datos, name="create_datos"),
    path("create_licencias/",create_licencias, name="create_licencias")
]
