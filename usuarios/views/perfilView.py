from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from usuarios.models import Usuario
from usuarios.forms import PerfilForm


class PerfilUpdateView(LoginRequiredMixin, UpdateView):
    model = Usuario
    form_class = PerfilForm
    template_name = 'web/perfil.html'
    success_url = reverse_lazy('perfil')
    
    def get_object(self, queryset=None):
        return self.request.user
    
    # def form_valid(self, form):
    #     response = super().form_valid(form)
    #     messages.success(self.request, 'Acción realizada con éxito.')
    #     return response

