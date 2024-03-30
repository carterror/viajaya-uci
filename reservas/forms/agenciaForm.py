from django import forms
from ..models.agencia import Agencia
from django.core.exceptions import ValidationError

class AgenciaForm(forms.ModelForm):
    
    provincias = (
        ('La Habana', 'La Habana'),
        ('Granma', 'Granma'),
        ('Las Tunas', 'Las Tunas'),
        ('Villa Clara', 'Villa Clara'),
        ('Holguin', 'Holguin'),
        ('Camaguey', 'Camaguey'),
        ('Santiago de Cuba', 'Santiago de Cuba'),
        
    )
    
    nombre = forms.CharField(required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control my-2'}))
    provincia = forms.ChoiceField(choices=provincias, widget=forms.Select(attrs={'class': 'form-control my-2'}))
    telefono = forms.CharField(required=True, max_length=12, widget=forms.TextInput(attrs={'class': 'form-control my-2'}))
    direccion = forms.CharField(required=True, max_length=250, widget=forms.TextInput(attrs={'class': 'form-control my-2'}))
    
    class Meta:
        model = Agencia
        fields = ['nombre', 'provincia', 'telefono', 'direccion']
        
    def clean_nombre(self):
        data = self.cleaned_data["nombre"]
        if not data[0].isupper():
            raise ValidationError("Dato incorrecto.")
        
        return data
    
    def clean_telefono(self):
        data: str = self.cleaned_data["telefono"]
        if not data.isdigit() or 8 > len(data) or len(data) > 12:
            raise ValidationError("Dato incorrecto.")
        return data
    
    