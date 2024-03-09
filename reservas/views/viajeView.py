from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from reservas.models import Viaje
from reservas.forms import RutaForm, ViajeroForm, BuscarForm, AgenciaForm, PasajeForm

class ViajeListView(LoginRequiredMixin, ListView):
    model = Viaje
    context_object_name = 'viajes'
    template_name = 'viajes/lista_viajes.html'
    
class ViajeCreateView(LoginRequiredMixin, CreateView):
    pass

class ViajeUpdateView(LoginRequiredMixin, UpdateView):
    pass

class ViajeDeleteView(LoginRequiredMixin, DeleteView):
    pass