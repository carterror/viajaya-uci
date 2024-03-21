from django import forms
from ..models.viajero import Viajero

class ViajeroForm(forms.ModelForm):
    nombre = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control my-2'}))
    ci = forms.CharField(max_length=11, min_length=11, required=True, widget=forms.TextInput(attrs={'class': 'form-control my-2'}))

    class Meta:
        model = Viajero
        fields = ['nombre', 'ci']