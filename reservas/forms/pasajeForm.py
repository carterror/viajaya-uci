from django import forms
from ..models.pasaje import Pasaje
from ..models.ruta import Ruta


class PasajeForm(forms.ModelForm):
    origen = forms.ModelChoiceField(required=True,
                                    queryset=Ruta.objects.all(),
                                    widget=forms.Select(attrs={'class': 'form-control my-2'}),
                                    empty_label='Selecciona el Origen')
    destino = forms.ModelChoiceField(required=True,
                                    queryset=Ruta.objects.all(), 
                                    widget=forms.Select(attrs={'class': 'form-control my-2'}),
                                    empty_label='Selecciona el Destino')
    precio = forms.DecimalField(required=True, max_digits=10, decimal_places=2,
                                widget=forms.NumberInput(attrs={'class': 'form-control my-2'}))
    capacidad = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={'class': 'form-control my-2'}))
    fecha = forms.DateTimeField(required=True, widget=forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control my-2'}, format="%Y-%m-%dT%H:%M"))
    transporte = forms.ChoiceField(required=True, widget=forms.Select(attrs={'class': 'form-control my-2'}), choices=(
        ("AV", "Avión"),
        ("TR", "Tren"),
        ("BU", "Omnibús")
    ))
    
    class Meta:
        model = Pasaje
        fields = ['origen', 'destino', 'precio', 'capacidad', 'fecha', 'transporte']
