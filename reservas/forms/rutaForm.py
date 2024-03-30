from django import forms
from ..models.ruta import Ruta
from django.core.exceptions import ValidationError

class RutaForm(forms.ModelForm):
    lugar = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control my-2'}))
    
    class Meta:
        model = Ruta
        fields = ['lugar']
        
    def clean_lugar(self):
        data = self.cleaned_data["lugar"]
        
        ruta = Ruta.objects.get(lugar=data)
        if ruta:
            raise ValidationError('Ya existe Ruta con este Lugar.')
        
        return data
    