from django import forms
from ..models.agencia import Agencia

class AgenciaForm(forms.ModelForm):
    
    provincias = (
        ('La habana', 'La Habana'),
        ('Granma', 'Granma'),
        ('Las Tunas', 'Las Tunas'),
        ('Villa Clara', 'Villa Clara'),
        ('Holguin', 'Holgin'),
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