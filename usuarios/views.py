from ast import Pass
from multiprocessing import context
from django.shortcuts import render, redirect

from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth import login, logout, authenticate

from usuarios.forms import User_registration_form 

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)
                
                context = {"message":f"Bienvenido {username}!! :D"}
                return render(request, "index.html", context = context)
            
        form = AuthenticationForm()
        return render(request, "usuarios/login.html", {"error":"Usuario o Contraseña invalida", "form": form})
    
    elif request.method == "GET":
        form = AuthenticationForm()
    return render(request, "usuarios/login.html", {"form":form})


def registro(request):
    if request.method == "POST":
        form = User_registration_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
        else:
            context = {"errors":form.errors}
            form = User_registration_form
            context["form"] = form
            return render(request, "usuarios/registro.html", {"form":form}) 
        
        
    elif request.method == "GET":
        form= User_registration_form ()
        return render(request, "usuarios/registro.html", {"form":form})
        