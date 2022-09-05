from django.urls import path
from usuarios.views import login_request, registro 

urlpatterns = [
   path("login/", login_request, name="login"), 
   path("registro/", registro, name= "registro"),
   
]