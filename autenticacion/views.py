from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

from django.contrib.auth.forms import AuthenticationForm
from .form import CustomUserCreationForm,FormularioDireccion

# Create your views here.

class VRegistro(View):

   def get(self, request):
      form=CustomUserCreationForm()
      return render(request, "registro/registro.html",{"form":form})

   def post(self, request):
      form=CustomUserCreationForm(request.POST)
      formDireccion=FormularioDireccion(request.POST)
      if form.is_valid():
         usuario=form.save()
         direccion= formDireccion.save(commit=False)
         login(request, usuario)
         direccion.user = request.user
         direccion.save()
         return redirect('Inicio')
      else:
         for msg in form.error_messages:
            messages.error(request, form.error_messages[msg])

         return render(request,"registro/registro.html",{"form":form})

   
def cerrar_sesion(request):
   logout(request)

   return redirect('Inicio')

def logear(request):
   if request.method=="POST":
      form=AuthenticationForm(request, data=request.POST)
      if form.is_valid():
         nombre_usuario=form.cleaned_data.get("username")
         contraseña=form.cleaned_data.get("password")
         usuario=authenticate(username=nombre_usuario, password=contraseña)
         if usuario is not None:
            login(request, usuario)
            return redirect('Inicio')
         else:
            messages.error(request, "usuario no valido o contraseña incorrecta")
      else:
         messages.error(request, "usuario no valido o contraseña incorrecta")

   form=AuthenticationForm()
   return render(request,"login/login.html",{"form":form})