from django.shortcuts import render, redirect, get_object_or_404
from reservas.models import Ruta, Viajero, Agencia, Pasaje
from reservas.forms import RutaForm, ViajeroForm, BuscarForm, AgenciaForm, PasajeForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

@login_required
def home(request):
    return render(request, 'home.html')

class RutaListView(LoginRequiredMixin, ListView):
    model = Ruta
    template_name = 'ruta/lista_ruta.html'
    context_object_name = 'rutas'

class RutaCreateView(LoginRequiredMixin, CreateView):
    model = Ruta
    form_class = RutaForm
    template_name = 'ruta/agregar_ruta.html'
    success_url = reverse_lazy('lista_rutas')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Ruta creado con éxito.')
        return response

class RutaUpdateView(LoginRequiredMixin, UpdateView):
    model = Ruta
    form_class = RutaForm
    template_name = 'ruta/editar_ruta.html'
    success_url = reverse_lazy('lista_rutas')

    def get_object(self):
        return get_object_or_404(Ruta, pk=self.kwargs.get('pk'))

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Ruta editado con éxito.')
        return response

class RutaDeleteView(LoginRequiredMixin, DeleteView):
    model = Ruta
    template_name = 'ruta/eliminar_ruta.html'
    success_url = reverse_lazy('lista_rutas')

    def get_object(self):
        return get_object_or_404(Ruta, pk=self.kwargs.get('pk'))

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Ruta eliminada con éxito.')
        return super().delete(request, *args, **kwargs)


class ViajeroListView(LoginRequiredMixin, ListView):
    model = Viajero
    template_name = "viajeros/lista_viajeros.html"
    context_object_name = "viajeros"

class ViajeroCreateView(LoginRequiredMixin, CreateView):
    model = Viajero
    form_class = ViajeroForm
    template_name = 'viajeros/agregar_viajero.html'
    success_url = reverse_lazy('lista_viajeros')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        response = super().form_valid(form)
        messages.success(self.request, 'Viajero creado con éxito.')
        return response

class ViajeroUpdateView(LoginRequiredMixin, UpdateView):
    model = Viajero
    form_class = ViajeroForm
    template_name = 'viajeros/editar_viajero.html'
    success_url = reverse_lazy('lista_viajeros')

    def get_object(self):
        return get_object_or_404(Viajero, pk=self.kwargs.get('pk'))

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Viajero editado con éxito.')
        return response
    
class ViajeroDeleteView(LoginRequiredMixin, DeleteView):
    model = Viajero
    template_name = 'viajeros/eliminar_viajero.html'
    success_url = reverse_lazy('lista_viajeros')

    def get_object(self):
        return get_object_or_404(Viajero, pk=self.kwargs.get('pk'))

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Viajero eliminado con éxito.')
        return super().delete(request, *args, **kwargs)


class AgenciaListView(LoginRequiredMixin, ListView):
    model = Agencia
    template_name = "agencias/lista_agencias.html"
    context_object_name = "agencias"
    
class AgenciaCreateView(LoginRequiredMixin, CreateView):
    model = Agencia
    form_class = AgenciaForm
    template_name = "agencias/agregar_agencia.html"
    success_url = reverse_lazy("lista_agencias")

    def form_valid(self, form):
        print('Validando Form')
        response = super().form_valid(form)
        messages.success(self.request, 'Agencia creada con éxito.')
        return response
    
class AgenciaUpdateView(LoginRequiredMixin, UpdateView):
    model = Agencia
    form_class = AgenciaForm
    template_name = 'agencias/editar_agencia.html'
    success_url = reverse_lazy('lista_agencias')

    def get_object(self):
        return get_object_or_404(Agencia, pk=self.kwargs.get('pk'))

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Agencia editada con éxito.')
        return response

class AgenciaDeleteView(LoginRequiredMixin, DeleteView):
    model = Agencia
    template_name = 'agencias/eliminar_agencia.html'
    success_url = reverse_lazy('lista_agencias')

    def get_object(self):
        return get_object_or_404(Agencia, pk=self.kwargs.get('pk'))

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Agencia eliminada con éxito.')
        return super().delete(request, *args, **kwargs)

class PasajeListView(LoginRequiredMixin, ListView):
    model = Pasaje
    template_name = "pasajes/lista_pasajes.html"
    context_object_name = "pasajes"
    
class PasajeCreateView(LoginRequiredMixin, CreateView):
    model = Pasaje
    form_class = PasajeForm
    template_name = "pasajes/agregar_pasaje.html"
    success_url = reverse_lazy("lista_pasajes")
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Pasaje creado con éxito.")
        return response
    
class PasajeUpdateView(LoginRequiredMixin, UpdateView):
    model = Pasaje
    form_class = PasajeForm
    template_name = "pasajes/editar_pasaje.html"
    success_url = reverse_lazy("lista_pasajes")
    
    def get_object(self):
        return get_object_or_404(Pasaje, pk=self.kwargs.get('pk'))

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Pasaje editado con éxito.')
        return response
    
class PasajeDeleteView(LoginRequiredMixin, DeleteView):
    model = Pasaje
    template_name = 'pasajes/eliminar_pasaje.html'
    success_url = reverse_lazy('lista_pasajes')

    def get_object(self):
        return get_object_or_404(Pasaje, pk=self.kwargs.get('pk'))

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Pasaje eliminado con éxito.')
        return super().delete(request, *args, **kwargs)