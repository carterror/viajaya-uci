from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from reservas.models import Agencia
from reservas.forms import AgenciaForm


class AgenciaListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Agencia
    template_name = "agencias/lista_agencias.html"
    context_object_name = "agencias"
    
    def test_func(self):
        return self.request.user.is_staff
    
class AgenciaCreateView(LoginRequiredMixin, CreateView):
    # permission_required = ('catalog.can_mark_returned', 'catalog.can_edit')
    model = Agencia
    form_class = AgenciaForm
    template_name = "agencias/agregar_agencia.html"
    success_url = reverse_lazy("lista_agencias")

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Acción realizada con éxito.')
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
        messages.success(self.request, 'Acción realizada con éxito.')
        return response

class AgenciaDeleteView(LoginRequiredMixin, DeleteView):
    model = Agencia
    template_name = 'agencias/eliminar_agencia.html'
    success_url = reverse_lazy('lista_agencias')

    def get_object(self):
        return get_object_or_404(Agencia, pk=self.kwargs.get('pk'))

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Acción realizada con éxito.')
        return super().delete(request, *args, **kwargs)
