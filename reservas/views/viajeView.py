from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from reservas.models.pasaje import Viaje
from reservas.forms.viajeForm import ViajeForm

class ViajeListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Viaje
    context_object_name = 'viajes'
    template_name = 'viajes/lista_viajes.html'
    
    @csrf_exempt
    def post(self, request, *args, **kwargs):
        ids = self.request.POST.getlist('ids[]')
        if ids:
            ids = [int(id) for id in ids]
            Viaje.objects.filter(id__in=ids).delete()
            messages.success(self.request, 'Acción realizada con éxito.')
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'error', 'message': 'No se proporcionaron IDs'})
    
    def test_func(self):
        return self.request.user.is_staff
    
class ViajeCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Viaje
    form_class = ViajeForm
    template_name = 'viajes/agregar_viaje.html'
    success_url = reverse_lazy('lista_viajes')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        response = super().form_valid(form)
        messages.success(self.request, 'Acción realizada con éxito.')
        return response
    
    def test_func(self):
        return self.request.user.is_staff

class ViajeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Viaje
    form_class = ViajeForm
    template_name = 'viajes/editar_viaje.html'
    success_url = reverse_lazy('lista_viajes')

    def test_func(self):
        return self.request.user.is_staff

class ViajeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Viaje
    template_name = 'viajes/eliminar_viaje.html'
    success_url = reverse_lazy('lista_viajes')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Acción realizada con éxito.')
        return super().delete(request, *args, **kwargs)
    
    def test_func(self):
        return self.request.user.is_staff