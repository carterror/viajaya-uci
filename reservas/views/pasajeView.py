from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from reservas.models.pasaje import Pasaje
from reservas.forms.pasajeForm import PasajeForm


class PasajeListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Pasaje
    template_name = "pasajes/lista_pasajes.html"
    context_object_name = "pasajes"
    
    @csrf_exempt
    def post(self, request, *args, **kwargs):
        ids = self.request.POST.getlist('ids[]')
        if ids:
            ids = [int(id) for id in ids]
            Pasaje.objects.filter(id__in=ids).delete()
            messages.success(self.request, 'Acción realizada con éxito.')
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'error', 'message': 'No se proporcionaron IDs'})
    
    def test_func(self):
        return self.request.user.is_staff
    
class PasajeCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Pasaje
    form_class = PasajeForm
    template_name = "pasajes/agregar_pasaje.html"
    success_url = reverse_lazy("lista_pasajes")
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Acción realizada con éxito.")
        return response
    
    def test_func(self):
        return self.request.user.is_staff
    
class PasajeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Pasaje
    form_class = PasajeForm
    template_name = "pasajes/editar_pasaje.html"
    success_url = reverse_lazy("lista_pasajes")

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Acción realizada con éxito.')
        return response
    
    def test_func(self):
        return self.request.user.is_staff
    
class PasajeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Pasaje
    template_name = 'pasajes/eliminar_pasaje.html'
    success_url = reverse_lazy('lista_pasajes')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Acción realizada con éxito.')
        return super().delete(request, *args, **kwargs)
    
    def test_func(self):
        return self.request.user.is_staff