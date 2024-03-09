from django import forms
from web.models import Notice


class NoticeForm(forms.ModelForm):
    titulo = forms.CharField(required=True, label='Titulo', min_length=6, max_length=100,
                             widget=forms.TextInput(attrs={'class': 'form-control my-2'}))
    descripcion = forms.CharField(label='Descripcion',
                                  widget=forms.TextInput(attrs={'class': 'form-control my-2'}))
    active = forms.BooleanField(required=False ,label='Activo', widget=forms.CheckboxInput(attrs={'class': 'my-2 form-check-label'}))
    
    class Meta:
        model = Notice
        fields = ['titulo', 'descripcion', 'active']