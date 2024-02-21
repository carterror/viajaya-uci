from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from reservas.models import Ruta, Viaje, Pasaje
from django.db.models.functions import TruncDate

# Create your views here.
def home(request):
    transport_curiosities = [
        {'curiosity': 'El primer avión de pasajeros voló en  1908.', 'source': 'Historia del Avión'},
        {'curiosity': 'El primer automóvil de producción en masa fue el Ford Model T, lanzado en  1908.', 'source': 'Historia del Automóvil'},
        {'curiosity': 'El primer tren de alta velocidad, el Shinkansen, comenzó a operar en Japón en  1964.', 'source': 'Historia del Tren'},
        {'curiosity': 'El primer sistema de metro subterráneo fue inaugurado en Londres en  1863.', 'source': 'Historia del Metro'},
        {'curiosity': 'El primer ferry de hidrógeno, el "Hyperion", comenzó a operar en  2021.', 'source': 'Innovaciones en Transporte'},
    ]
    rutas = Ruta.objects.all()
    
    context = {'rutas': rutas, 'transport_curiosities': transport_curiosities}
    
    return render(request, 'web/home.html', context)

def buscar(request):
    if request.method == 'POST':
        pasajes = Pasaje.objects.annotate(fecha_truncada=TruncDate('fecha')).filter(origen=request.POST['origen'], destino=request.POST['destino'], fecha_truncada=request.POST['fecha'])
        
        
        return render(request, 'web/pasaje.html', {'pasajes': pasajes})
    else:
        rutas = Ruta.objects.all()
        return render(request, 'web/buscar.html', {'rutas': rutas})
    