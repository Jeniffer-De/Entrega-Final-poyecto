from pathlib import Path
from django.contrib import admin
from django.urls import path
from portal_empleados.views import inicio

urlpatterns = [
    path('admin/', admin.site.urls),
    path("inicio/",inicio, name="inicio")
]
