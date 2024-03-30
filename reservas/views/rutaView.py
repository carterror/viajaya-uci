from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

from reservas.models.ruta import Ruta
from ..forms.rutaForm import RutaForm


class RutaListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Ruta
    template_name = 'ruta/lista_ruta.html'
    context_object_name = 'rutas'
    
    @csrf_exempt
    def post(self, request, *args, **kwargs):
        ids = self.request.POST.getlist('ids[]')
        if ids:
            ids = [int(id) for id in ids]
            Ruta.objects.filter(id__in=ids).delete()
            messages.success(self.request, 'Acción realizada con éxito.')
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'error', 'message': 'No se proporcionaron IDs'})
    
    def test_func(self):
        return self.request.user.is_staff

class RutaCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Ruta
    form_class = RutaForm
    template_name = 'ruta/agregar_ruta.html'
    success_url = reverse_lazy('lista_rutas')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Acción realizada con éxito.')
        return response
    
    def test_func(self):
        return self.request.user.is_staff

class RutaUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Ruta
    form_class = RutaForm
    template_name = 'ruta/editar_ruta.html'
    success_url = reverse_lazy('lista_rutas')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Acción realizada con éxito.')
        return response
    
    def test_func(self):
        return self.request.user.is_staff

class RutaDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Ruta
    template_name = 'ruta/eliminar_ruta.html'
    success_url = reverse_lazy('lista_rutas')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Acción realizada con éxito.')
        return super().delete(request, *args, **kwargs)
    
    def test_func(self):
        return self.request.user.is_staff

