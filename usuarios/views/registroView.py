from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect

# Create your views here.
# usuarios/views.py
from reservas.models.viajero import Viajero
from django.contrib.auth import login, authenticate
from usuarios.forms import RegistroUsuarioForm

@csrf_protect
def registro(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            viajero = Viajero()
            viajero.nombre = form.cleaned_data.get('first_name')
            viajero.ci = form.cleaned_data.get('ci')
            viajero.user = user
            viajero.save()
            return redirect('/')
    else:
        form = RegistroUsuarioForm()
        
    return render(request, 'auth/register.html', {'form': form})