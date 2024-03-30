from django import forms
from ..models.pasaje import Viaje
from ..models.viajero import Viajero
from reservas.models.pasaje import Pasaje
from usuarios.models import Usuario


class ViajeForm(forms.ModelForm):
    
    pasaje = forms.ModelChoiceField(required=True,
                                    queryset=Pasaje.objects.all(),
                                    widget=forms.Select(attrs={'class': 'form-control my-2'}),
                                    label='Pasaje',
                                    empty_label='Selecciona el Pasaje')
    user = forms.ModelChoiceField(required=True,
                                    queryset=Usuario.objects.all(),
                                    widget=forms.Select(attrs={'class': 'form-control my-2'}),
                                    label='Usuario',
                                    empty_label='Selecciona el Usuario')
    viajero = forms.ModelChoiceField(required=True,
                                    queryset=Viajero.objects.all(),
                                    widget=forms.Select(attrs={'class': 'form-control my-2'}),
                                    label='Viajero',
                                    empty_label='Selecciona el Viajero')
    
    estado = forms.ChoiceField(required=True, widget=forms.Select(attrs={'class': 'form-control my-2'},),
                               choices=(
                                        ("activa", "Activa"),
                                        ("proxima",  "Próxima"),
                                        ("realizada",  "Realizada"),
                                        ("cancelada", "Cancelada"),
                                    ),
                               label='Selecciona el estado'
                               )
    
    
    class Meta:
        model = Viaje
        fields = ['pasaje', 'user', 'viajero', 'estado']