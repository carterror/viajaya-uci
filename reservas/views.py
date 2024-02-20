from django.shortcuts import render, redirect, get_object_or_404
from reservas.models import Ruta, Viajero
from reservas.forms import RutaForm, ViajeroForm, BuscarForm
from django.contrib import messages


def home(request):
    return render(request, 'home.html')


# Create your views here.
def lista_rutas(request):
    rutas = Ruta.objects.all()
    return render(request, 'ruta/lista_ruta.html', {'rutas': rutas})


def agregar_ruta(request):
    if request.method == "POST":
        form = RutaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ruta creado con éxito.')
            return redirect('lista_rutas')
    else:
        form = RutaForm()
    return render(request, 'ruta/agregar_ruta.html', {'form': form})


def editar_ruta(request, pk):
    ruta = get_object_or_404(Ruta, pk=pk)
    if request.method == "POST":
        form = RutaForm(request.POST,instance=ruta)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ruta editado con éxito.')
            return redirect('lista_rutas')
    else:
        form = RutaForm(instance=ruta)
    return render(request, 'ruta/editar_ruta.html', {'form': form, 'ruta': ruta})


def eliminar_ruta(request, pk):
    ruta = get_object_or_404(Ruta, pk=pk)

    if request.method == "POST":
        ruta.delete()
        messages.success(request, 'Ruta eliminada con éxito.')
        return redirect('lista_rutas')

    return render(request, 'ruta/eliminar_ruta.html', {'ruta': ruta})


def lista_viajeros(request):
    viajeros = Viajero.objects.all()
    return render(request, 'viajeros/lista_viajeros.html', {'viajeros': viajeros})


def agregar_viajero(request):
    if request.method == "POST":
        form = ViajeroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Viajero creado con exito.')
            return redirect('lista_viajeros')
    else:
        form = ViajeroForm()
    return render(request, 'viajeros/agregar_viajeros.html', {'form': form})


def editar_viajero(request, pk):
    viajero = get_object_or_404(Viajero, pk=pk)
    if request.method == "POST":
        form = ViajeroForm(request.POST,instance=viajero)
        if form.is_valid():
            form.save()
            messages.success(request, 'Viajero editado con éxito.')
            return redirect('lista_viajeros')
    else:
        form = ViajeroForm(instance=viajero)
    return render(request, 'viajeros/editar_viajeros.html', {'form': form, 'ruta': viajero})


def eliminar_viajero(request, pk):
    viajero = get_object_or_404(Viajero, pk=pk)

    if request.method == "POST":
        viajero.delete()
        messages.success(request, 'Viajero eliminado con éxito.')
        return redirect('lista_viajeros')

    return render(request, 'viajeros/eliminar_viajeros.html', {'viajero': viajero})

def buscar_viajero(request):
    if 'query' in request.GET:
        form = BuscarForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            viajeros = Viajero.objects.filter(nombre__icontains=query)
    else:
        form = BuscarForm()
        viajeros = []

    return render(request, 'viajeros/lista_viajeros.html', {'viajeros': viajeros})

def lista_agencias(request):
    pass

def agregar_agencia(request):
    pass

def editar_agencia(request):
    pass

def eliminar_agencia(request):
    pass