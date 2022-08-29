from pathlib import Path
from django.contrib import admin
from django.urls import path
from portal_empleados.views import inicio
from acerca_de.views import create_informacion
from datos.views import datos_personal
from licencias.views import licencias

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/',inicio, name='inicio'),
    path('create_informacion/',create_informacion, name='create_informacion'),
    path("datos_personal/",datos_personal, name="datos_personal"),
    path("licencias/",licencias, name="licencias")
]
