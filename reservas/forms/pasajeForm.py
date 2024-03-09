from django import forms
from ..models import Pasaje, Ruta

class PasajeForm(forms.ModelForm):
    origen = forms.ModelChoiceField(required=True,queryset=Ruta.objects.all(), widget=forms.Select(attrs={'class': 'form-control my-2'}))
    destino = forms.ModelChoiceField(required=True, queryset=Ruta.objects.all(), widget=forms.Select(attrs={'class': 'form-control my-2'}))
    precio = forms.DecimalField(required=True, max_digits=10, decimal_places=2)
    capacidad = forms.IntegerField(required=True)
    fecha = forms.DateTimeField(required=True, widget=forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control my-2'}))
    transporte = forms.ChoiceField(required=True, widget=forms.Select(attrs={'class': 'form-control my-2'}), choices=(
        ("AV", "Avión"),
        ("TR", "Tren"),
        ("BU", "Omnibús")
    ))
    
    class Meta:
        model = Pasaje
        fields = ['origen', 'destino', 'precio', 'capacidad', 'fecha', 'transporte']
