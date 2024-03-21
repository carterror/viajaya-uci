from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView
from reservas.models import Viaje

class ReservaListView(ListView):
    model = Viaje
    template_name = ".html"
    
class ResrevaCreateView(CreateView):
    model = Viaje
    
    template_name = ".html"
    
class ReservaUpdateView(UpdateView):
    model = Viaje
    template_name = ".html"
    
class ReservaDeleteView(DeleteView):
    model = Viaje
    template_name = ".html"




