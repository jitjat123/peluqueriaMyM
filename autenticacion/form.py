from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Direccion

class CustomUserCreationForm(UserCreationForm):
    ciudad = forms.CharField(max_length=50, required=False)
    departamento = forms.CharField(max_length=50, required=False)
    direccion = forms.CharField(max_length=255, required=False)

    class Meta:
        model= User
        fields= ["username", "email", "password1", "password2"]


class FormularioDireccion(forms.ModelForm):
    ciudad = forms.CharField(max_length=50, required=False)
    departamento = forms.CharField(max_length=50, required=False)
    direccion = forms.CharField(max_length=255, required=False)


    class Meta:
        model= Direccion
        fields= ["ciudad","departamento","direccion"]