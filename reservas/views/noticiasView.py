from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from web.models import Notice
from reservas.forms import NoticeForm

class NoticiaListView(LoginRequiredMixin, ListView):
    model = Notice
    context_object_name = 'noticias'
    template_name = 'noticias/lista_noticias.html'
    
class NoticiaCreateView(LoginRequiredMixin, CreateView):
    model = Notice
    form_class = NoticeForm
    template_name = 'noticias/agregar_noticia.html'
    success_url = reverse_lazy('lista_noticias')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Acción realizada con éxito.")
        return response
    
class NoticiaUpdateView(LoginRequiredMixin, UpdateView):
    model = Notice
    form_class = NoticeForm
    template_name = 'noticias/editar_noticia.html'
    success_url = reverse_lazy('lista_noticias')
    
    def get_object(self):
        return get_object_or_404(Notice, pk=self.kwargs.get('pk'))
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Acción realizada con éxito.')
        return response
    
class NoticiaDeleteView(LoginRequiredMixin, DeleteView):
    model = Notice
    template_name = 'noticias/eliminar_noticia.html'
    success_url = reverse_lazy('lista_noticias')

    def get_object(self):
        return get_object_or_404(Notice, pk=self.kwargs.get('pk'))

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Acción realizada con éxito.')
        return super().delete(request, *args, **kwargs)