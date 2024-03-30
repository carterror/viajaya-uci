from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Count, Sum, F
from django.utils import timezone
from reservas.models.pasaje import Pasaje, Viaje


class HomeView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    template_name = "home.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        hoy = timezone.now().date()

        # Realiza la consulta
        pasajes_vendidos = Pasaje.objects.filter(
            viaje__created_at__date=hoy # Filtra los viajes creados hoy
        ).annotate(
            cantidad_vendida=Count('viaje'), # Cuenta cuántos viajes hay para cada pasaje
            dinero_total=Sum('precio') # Suma los precios de los pasajes
        ).order_by('-cantidad_vendida') # Ordena por la cantidad vendida en orden descendente
        
        context["pasajes"] = pasajes_vendidos
        return context
    
    def test_func(self):
        return self.request.user.is_staff