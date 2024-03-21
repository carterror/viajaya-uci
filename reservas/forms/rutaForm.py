from django import forms
from ..models.ruta import Ruta

class RutaForm(forms.ModelForm):
    lugar = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control my-2'}))
    
    class Meta:
        model = Ruta
        fields = ['lugar']