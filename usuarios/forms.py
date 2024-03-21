# usuarios/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from usuarios.models import Usuario


class RegistroUsuarioForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields="__all__"
        
class PerfilForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}),
                                 label="Nombre")
    username = forms.CharField(min_length=5,
                               widget=forms.TextInput(attrs={"class": "form-control"}),
                               label="Nombre de Usuario")
    ci = forms.CharField(min_length=11,
                         max_length=11,
                         widget=forms.NumberInput(attrs={"class": "form-control", "pattern": "^\d{11}$"}),
                         label="Carnet de Identidad"
                         )
    email = forms.EmailField(disabled=True, widget=forms.EmailInput(attrs={"class": "form-control"}))
    class Meta:
        model = Usuario
        fields = ["first_name", "username", "ci", "email"]
