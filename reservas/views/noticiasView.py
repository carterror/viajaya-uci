from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from web.models import Notice
from reservas.forms.noticiaForm import NoticeForm

class NoticiaListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Notice
    context_object_name = 'noticias'
    template_name = 'noticias/lista_noticias.html'
    
    def test_func(self):
        return self.request.user.is_staff
    
class NoticiaCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Notice
    form_class = NoticeForm
    template_name = 'noticias/agregar_noticia.html'
    success_url = reverse_lazy('lista_noticias')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Acción realizada con éxito.")
        return response
    
    def test_func(self):
        return self.request.user.is_staff
    
class NoticiaUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
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
    
    def test_func(self):
        return self.request.user.is_staff
    
class NoticiaDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Notice
    template_name = 'noticias/eliminar_noticia.html'
    success_url = reverse_lazy('lista_noticias')

    def get_object(self):
        return get_object_or_404(Notice, pk=self.kwargs.get('pk'))

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Acción realizada con éxito.')
        return super().delete(request, *args, **kwargs)
    
    def test_func(self):
        return self.request.user.is_staff