from django.shortcuts import render, redirect, get_object_or_404
from reservas.models import Ruta, Viajero, Agencia, Pasaje
from reservas.forms import RutaForm, ViajeroForm, BuscarForm, AgenciaForm, PasajeForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect


@login_required
def home(request):
    return render(request, 'home.html')


class RutaView():
# Create your views here.
    @login_required
    def lista_rutas(request):
        rutas = Ruta.objects.all()
        return render(request, 'ruta/lista_ruta.html', {'rutas': rutas})

    @csrf_protect
    @login_required
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


    @csrf_protect
    @login_required
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


    @login_required
    def eliminar_ruta(request, pk):
        ruta = get_object_or_404(Ruta, pk=pk)

        if request.method == "POST":
            ruta.delete()
            messages.success(request, 'Ruta eliminada con éxito.')
            return redirect('lista_rutas')

        return render(request, 'ruta/eliminar_ruta.html', {'ruta': ruta})


class ViajeroView():

    @login_required
    def lista_viajeros(request):
        viajeros = Viajero.objects.all()
        return render(request, 'viajeros/lista_viajeros.html', {'viajeros': viajeros})


    @csrf_protect
    @login_required
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


    @csrf_protect
    @login_required
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


    @login_required
    def eliminar_viajero(request, pk):
        viajero = get_object_or_404(Viajero, pk=pk)

        if request.method == "POST":
            viajero.delete()
            messages.success(request, 'Viajero eliminado con éxito.')
            return redirect('lista_viajeros')

        return render(request, 'viajeros/eliminar_viajeros.html', {'viajero': viajero})

    @login_required
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


class AgenciaView():
    @login_required
    def lista_agencias(request):
        agencias = Agencia.objects.all()
        return render(request, 'agencias/lista_agencias.html', {'agencias': agencias})


    @csrf_protect
    @login_required
    def agregar_agencia(request):
        if request.method == "POST":
            form = AgenciaForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Agencia creado con exito.')
                return redirect('lista_agencias')
        else:
            form = AgenciaForm()
        return render(request, 'agencias/agregar_agencia.html', {'form': form})

    @csrf_protect
    @login_required
    def editar_agencia(request, pk):
        agencia = get_object_or_404(Agencia, pk=pk)
        if request.method == "POST":
            form = AgenciaForm(request.POST,instance=agencia)
            if form.is_valid():
                form.save()
                messages.success(request, 'Agencia editada con éxito.')
                return redirect('lista_agencias')
        else:
            form = AgenciaForm(instance=agencia)
        return render(request, 'agencias/editar_agencia.html', {'form': form, 'ruta': agencia})

    @login_required
    def eliminar_agencia(request, pk):
        agencia = get_object_or_404(Agencia, pk=pk)

        if request.method == "POST":
            agencia.delete()
            messages.success(request, 'Agencia eliminada con éxito.')
            return redirect('lista_agencias')

        return render(request, 'agencias/eliminar_agencia.html', {'agencia': agencia})
    
class PasajeView():
    
    @login_required
    def lista_pasajes(request):
        pasajes = Pasaje.objects.all()
        return render(request, 'pasajes/lista_pasajes.html', {'pasajes': pasajes})


    @csrf_protect
    @login_required
    def agregar_pasaje(request):
        if request.method == "POST":
            form = PasajeForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Pasaje creado con exito.')
                return redirect('lista_pasajes')
        else:
            form = PasajeForm()
        return render(request, 'pasajes/agregar_pasaje.html', {'form': form})

    @csrf_protect
    @login_required
    def editar_pasaje(request, pk):
        pasaje = get_object_or_404(Pasaje, pk=pk)
        if request.method == "POST":
            form = PasajeForm(request.POST,instance=pasaje)
            if form.is_valid():
                form.save()
                messages.success(request, 'Pasajes editado con éxito.')
                return redirect('lista_pasajes')
        else:
            form = PasajeForm(instance=pasaje)
        return render(request, 'pasajes/editar_pasaje.html', {'form': form, 'ruta': pasaje})

    @login_required
    def eliminar_pasaje(request, pk):
        pasaje = get_object_or_404(Pasaje, pk=pk)

        if request.method == "POST":
            pasaje.delete()
            messages.success(request, 'Pasaje eliminado con éxito.')
            return redirect('lista_pasajes')

        return render(request, 'pasajes/eliminar_pasaje.html', {'pasaje': pasaje})
    