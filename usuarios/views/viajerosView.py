from reservas.models import Viajero
from reservas.forms import ViajeroForm
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect


class ViajeroListView(LoginRequiredMixin, ListView):
    model = Viajero
    context_object_name = 'viajeros'
    template_name = 'web/viajeros.html'
    
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
    