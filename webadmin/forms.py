from django import forms
from .models import *

#Creacion de los forms por Modelo

class UsuarioLoginForm(forms.ModelForm):

    class Meta:
        model = Usuario
        fields = ('usuario', 'password', )

class UsuarioRegisterForm(forms.ModelForm):

    class Meta:
        model = Usuario
        fields = ('usuario', 'password', 'nombres', 'apellidos', 'correo', )