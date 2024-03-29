from reservas.models.viajero import Viajero
from reservas.forms.viajeroForm import ViajeroForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages


class ViajeroListView(LoginRequiredMixin, ListView):
    model = Viajero
    context_object_name = 'viajeros'
    template_name = 'web/viajeros/lista_viajeros.html'
    
    def get_queryset(self):
        user = self.request.user
        return Viajero.objects.filter(user=user)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ViajeroForm()
        return context

class ViajeroCreateView(LoginRequiredMixin, CreateView):
    model = Viajero
    form_class = ViajeroForm
    template_name = 'web/viajeros/agregar_viajero.html'
    success_url = reverse_lazy('list_viajeros')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        response = super().form_valid(form)
        messages.success(self.request, 'Acción realizada con éxito.')
        return response
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'request': self.request})
        return kwargs
    
class ViajeroUpdateView(LoginRequiredMixin, UpdateView):
    model = Viajero
    form_class = ViajeroForm
    template_name = 'web/viajeros/editar_viajero.html'
    success_url = reverse_lazy('list_viajeros')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'request': self.request})
        return kwargs

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Acción realizada con éxito.')
        return response
    
    
class ViajeroDeleteView(LoginRequiredMixin, DeleteView):
    model = Viajero
    template_name = 'web/viajeros/eliminar_viajero.html'
    context_object_name = 'viajero'
    success_url = reverse_lazy('list_viajeros')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Acción realizada con éxito.')
        return super().delete(request, *args, **kwargs)