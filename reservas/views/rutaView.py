from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404

from reservas.models import Ruta
from ..forms import RutaForm


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
        messages.success(self.request, 'Acción realizada con éxito.')
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
        messages.success(self.request, 'Acción realizada con éxito.')
        return response

class RutaDeleteView(LoginRequiredMixin, DeleteView):
    model = Ruta
    template_name = 'ruta/eliminar_ruta.html'
    success_url = reverse_lazy('lista_rutas')

    def get_object(self):
        return get_object_or_404(Ruta, pk=self.kwargs.get('pk'))

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Acción realizada con éxito.')
        return super().delete(request, *args, **kwargs)

