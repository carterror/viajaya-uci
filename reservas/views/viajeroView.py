from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from reservas.models import Ruta, Viajero, Agencia, Pasaje
from reservas.forms import RutaForm, ViajeroForm, BuscarForm, AgenciaForm, PasajeForm

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
        messages.success(self.request, 'Acción realizada con éxito.')
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
        messages.success(self.request, 'Acción realizada con éxito.')
        return response
    
class ViajeroDeleteView(LoginRequiredMixin, DeleteView):
    model = Viajero
    template_name = 'viajeros/eliminar_viajero.html'
    success_url = reverse_lazy('lista_viajeros')

    def get_object(self):
        return get_object_or_404(Viajero, pk=self.kwargs.get('pk'))

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Acción realizada con éxito.')
        return super().delete(request, *args, **kwargs)

