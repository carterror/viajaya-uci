# gestion_impresoras/forms.py

from django import forms
from django.core.exceptions import ValidationError

from reservas.models import Ruta, Viajero, Agencia, Pasaje

def validate_only_numbers(value):
    if not value.isdigit():
        raise ValidationError("Este campo solo acepta números.")

class RutaForm(forms.ModelForm):
    lugar = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control my-2'}))
    
    class Meta:
        model = Ruta
        fields = ['lugar']
        
class ViajeroForm(forms.ModelForm):
    nombre = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control my-2'}))
    ci = forms.CharField(max_length=11, min_length=11, required=True, widget=forms.TextInput(attrs={'class': 'form-control my-2'}))

    class Meta:
        model = Viajero
        fields = ['nombre', 'ci']
        

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

class PasajeForm(forms.ModelForm):
    origen = forms.ModelChoiceField(required=True,queryset=Ruta.objects.all(), widget=forms.Select(attrs={'data-placeholder': 'Selecciona el origen','class': 'form-control my-2'}))
    destino = forms.ModelChoiceField(required=True, queryset=Ruta.objects.all(), widget=forms.Select(attrs={'data-placeholder': 'Selecciona el destino','class': 'form-control my-2'}))
    precio = forms.DecimalField(required=True, max_digits=10, decimal_places=2)
    capacidad = forms.IntegerField(required=True)
    fecha = forms.DateTimeField(required=True)
    transporte = forms.ChoiceField(required=True, widget=forms.Select(attrs={'class': 'form-control my-2'}), choices=(
        ("AV", "Avión"),
        ("TR", "Tren"),
        ("BU", "Omnibús")
    ))
    
    class Meta:
        model = Pasaje
        fields = ['origen', 'destino', 'precio', 'capacidad', 'fecha', 'transporte']


class BuscarForm(forms.Form):
    query = forms.CharField(label='Buscar', max_length=100)

# class ImpresoraForm(forms.ModelForm):
#     nombre = forms.CharField(required=True,
#                              widget=forms.TextInput(attrs={'class': 'form-control my-2 col-md-6'}))
#     tipo_conexion = forms.ChoiceField(required=True, choices=(
#         ('USB', 'USB'),
#         ('SERIAL', 'SERIAL'),
#         ('WIFI', 'WIFI'),
#     ),
#                                       widget=forms.Select(attrs={'class': 'form-select my-2'})
#                                       )
#     descripcion = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control my-2'}))
#     localizacion = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control my-2'}))
#     marca = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control my-2'}))
#     modelo_fabricacion = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control my-2'}))
#     local = forms.ModelChoiceField(required=True,
#                                    widget=forms.Select(attrs={'class': 'form-select my-2'}),
#                                    queryset=Local.objects.all(),
#                                    empty_label="Selecciona un Impresora")

#     class Meta:
#         model = Impresora
#         fields = [
#             'nombre',
#             'tipo_conexion',
#             'descripcion',
#             'localizacion',
#             'marca',
#             'modelo_fabricacion',
#             'local']

#     def __init__(self, *args, **kwargs):
#         self.impresora_id = kwargs.pop('impresora_id', None)
#         super(ImpresoraForm, self).__init__(*args, **kwargs)
