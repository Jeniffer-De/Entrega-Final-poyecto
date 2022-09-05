from re import template
from django.urls import path
from usuarios.views import login_request, registro 
from django.contrib.auth.views import LogoutView

urlpatterns = [
   path("login/", login_request, name="login"), 
   path("registro/", registro, name= "registro"),
   path("logout/", LogoutView.as_view(template_name="usuarios/logout.html"), name="Logout")
   
]