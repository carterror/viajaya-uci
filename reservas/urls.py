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

from reservas.views import *

urlpatterns = [
    path('', home, name='dashboard'),
    
    path('rutas/', RutaListView.as_view(), name='lista_rutas'),
    path('rutas/agregar/', RutaCreateView.as_view(), name='agregar_ruta'),
    path('rutas/<int:pk>/editar/', RutaUpdateView.as_view(), name='editar_ruta'),
    path('rutas/<int:pk>/eliminar/', RutaDeleteView.as_view(), name='eliminar_ruta'),

    path('viajeros/', ViajeroListView.as_view(), name='lista_viajeros'),
    path('viajeros/agregar/', ViajeroCreateView.as_view(), name='agregar_viajero'),
    path('viajeros/<int:pk>/editar/', ViajeroUpdateView.as_view(), name='editar_viajero'),
    path('viajeros/<int:pk>/eliminar/', ViajeroDeleteView.as_view(), name='eliminar_viajero'),

    path('agencias/', AgenciaListView.as_view(), name='lista_agencias'),
    path('agencias/agregar/', AgenciaCreateView.as_view(), name='agregar_agencia'),
    path('agencias/<int:pk>/editar/', AgenciaUpdateView.as_view(), name='editar_agencia'),
    path('agencias/<int:pk>/eliminar/', AgenciaDeleteView.as_view(), name='eliminar_agencia'),
    
    path('pasajes/', PasajeListView.as_view(), name='lista_pasajes'),
    path('pasajes/agregar/', PasajeCreateView.as_view(), name='agregar_pasaje'),
    path('pasajes/<int:pk>/editar/', PasajeUpdateView.as_view(), name='editar_pasaje'),
    path('pasajes/<int:pk>/eliminar/', PasajeDeleteView.as_view(), name='eliminar_pasaje'),
]
