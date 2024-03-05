from django import forms

from .rutaForm import RutaForm
from .agenciaForm import AgenciaForm
from .viajeroForm import ViajeroForm
from .pasajeForm import PasajeForm


class BuscarForm(forms.Form):
    query = forms.CharField(label='Buscar', max_length=100)