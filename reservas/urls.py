"""
URL configuration for localimpresion project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib.auth import views as auth_views
from django.urls import path, include

from reservas.views import (RutaView, ViajeroView,
                                 home, AgenciaView, PasajeView)

urlpatterns = [
    path('', home, name='dashboard'),
    
    path('rutas/', RutaView.lista_rutas, name='lista_rutas'),
    path('rutas/agregar/', RutaView.agregar_ruta, name='agregar_ruta'),
    path('rutas/<int:pk>/editar/', RutaView.editar_ruta, name='editar_ruta'),
    path('rutas/<int:pk>/eliminar/', RutaView.eliminar_ruta, name='eliminar_ruta'),

    path('viajeros/', ViajeroView.lista_viajeros, name='lista_viajeros'),
    path('viajeros/agregar/', ViajeroView.agregar_viajero, name='agregar_viajero'),
    path('viajeros/<int:pk>/editar/', ViajeroView.editar_viajero, name='editar_viajero'),
    path('viajeros/<int:pk>/eliminar/', ViajeroView.eliminar_viajero, name='eliminar_viajero'),
    # path('viajeros/buscar', buscar_viajero, name='buscar_viajero'),

    path('agencias/', AgenciaView.lista_agencias, name='lista_agencias'),
    path('agencias/agregar/', AgenciaView.agregar_agencia, name='agregar_agencia'),
    path('agencias/<int:pk>/editar/', AgenciaView.editar_agencia, name='editar_agencia'),
    path('agencias/<int:pk>/eliminar/', AgenciaView.eliminar_agencia, name='eliminar_agencia'),
    
    path('pasajes/', PasajeView.lista_pasajes, name='lista_pasajes'),
    path('pasajes/agregar/', PasajeView.agregar_pasaje, name='agregar_pasaje'),
    path('pasajes/<int:pk>/editar/', PasajeView.editar_pasaje, name='editar_pasaje'),
    path('pasajes/<int:pk>/eliminar/', PasajeView.eliminar_pasaje, name='eliminar_pasaje'),
]
