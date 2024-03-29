from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from reservas.models.viajero import Viajero
from reservas.forms.viajeroForm import ViajeroForm

class ViajeroListView(LoginRequiredMixin, UserPassesTestMixin,ListView):
    model = Viajero
    template_name = "viajeros/lista_viajeros.html"
    context_object_name = "viajeros"
    
    @csrf_exempt
    def post(self, request, *args, **kwargs):
        ids = self.request.POST.getlist('ids[]')
        if ids:
            ids = [int(id) for id in ids]
            Viajero.objects.filter(id__in=ids).delete()
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'error', 'message': 'No se proporcionaron IDs'})
    
    def test_func(self):
        return self.request.user.is_staff

class ViajeroCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Viajero
    form_class = ViajeroForm
    template_name = 'viajeros/agregar_viajero.html'
    success_url = reverse_lazy('lista_viajeros')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        response = super().form_valid(form)
        messages.success(self.request, 'Acción realizada con éxito.')
        return response
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'request': self.request})
        return kwargs
    
    def test_func(self):
        return self.request.user.is_staff

class ViajeroUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Viajero
    form_class = ViajeroForm
    template_name = 'viajeros/editar_viajero.html'
    success_url = reverse_lazy('lista_viajeros')
        
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Acción realizada con éxito.')
        return response
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'request': self.request})
        return kwargs
    
    def test_func(self):
        return self.request.user.is_staff
    
class ViajeroDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Viajero
    template_name = 'viajeros/eliminar_viajero.html'
    success_url = reverse_lazy('lista_viajeros')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Acción realizada con éxito.')
        return super().delete(request, *args, **kwargs)
    
    def test_func(self):
        return self.request.user.is_staff

