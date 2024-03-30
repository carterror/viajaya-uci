from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from reservas.models.agencia import Agencia
from reservas.forms.agenciaForm import AgenciaForm


class AgenciaListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Agencia
    template_name = "agencias/lista_agencias.html"
    context_object_name = "agencias"
    
    @csrf_exempt
    def post(self, request, *args, **kwargs):
        ids = self.request.POST.getlist('ids[]')
        if ids:
            ids = [int(id) for id in ids]
            Agencia.objects.filter(id__in=ids).delete()
            messages.success(self.request, 'Acción realizada con éxito.')
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'error', 'message': 'No se proporcionaron IDs'})
    
    def test_func(self):
        return self.request.user.is_staff
    
class AgenciaCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    # permission_required = ('catalog.can_mark_returned', 'catalog.can_edit')
    model = Agencia
    form_class = AgenciaForm
    template_name = "agencias/agregar_agencia.html"
    success_url = reverse_lazy("lista_agencias")

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Acción realizada con éxito.')
        return response
    
    def test_func(self):
        return self.request.user.is_staff
    
class AgenciaUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Agencia
    form_class = AgenciaForm
    template_name = 'agencias/editar_agencia.html'
    success_url = reverse_lazy('lista_agencias')

    def get_object(self):
        return get_object_or_404(Agencia, pk=self.kwargs.get('pk'))

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Acción realizada con éxito.')
        return response
    
    def test_func(self):
        return self.request.user.is_staff

class AgenciaDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Agencia
    template_name = 'agencias/eliminar_agencia.html'
    success_url = reverse_lazy('lista_agencias')

    def get_object(self):
        return get_object_or_404(Agencia, pk=self.kwargs.get('pk'))

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Acción realizada con éxito.')
        return super().delete(request, *args, **kwargs)
    
    def test_func(self):
        return self.request.user.is_staff
