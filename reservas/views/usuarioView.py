from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from usuarios.models import Usuario
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from usuarios.forms import PerfilForm

class UsuarioListView(LoginRequiredMixin, UserPassesTestMixin,ListView):
    model = Usuario
    template_name = "usuarios/lista_usuarios.html"
    context_object_name = "usuarios"
    
    @csrf_exempt
    def post(self, request, *args, **kwargs):
        ids = self.request.POST.getlist('ids[]')
        if ids:
            ids = [int(id) for id in ids]
            Usuario.objects.filter(id__in=ids).delete()
            messages.success(self.request, 'Acción realizada con éxito.')
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'error', 'message': 'No se proporcionaron IDs'})
    
    def test_func(self):
        return self.request.user.is_staff


class UsuarioUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Usuario
    form_class = PerfilForm
    template_name = 'usuarios/editar_usuario.html'
    success_url = reverse_lazy('lista_viajeros')
        
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Acción realizada con éxito.')
        return response
    
    def test_func(self):
        return self.request.user.is_staff
    
class UsuarioDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Usuario
    template_name = 'usuarios/eliminar_usuario.html'
    success_url = reverse_lazy('lista_usuarios')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Acción realizada con éxito.')
        return super().delete(request, *args, **kwargs)
    
    def test_func(self):
        return self.request.user.is_staff