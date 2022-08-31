from django.contrib import admin
from datos.models import datos 

#admin.site.register(datos)

@admin.register(datos)
class datos_admin(admin.ModelAdmin):
    list_display = ["nombre", "Cedula", "is_active"]
