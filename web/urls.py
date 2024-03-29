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
from django.contrib import admin
from django.urls import path

from web.views import home, buscar, AgenciaListView, ViajerosCompraView, DetallesCompraView, CompletadoView, ReservasListView

urlpatterns = [
    path('', home, name='home'),
    path('buscar/', buscar, name='buscar'),
    path('agencias/', AgenciaListView.as_view(), name='list_agencias'),
    
    path('reservar/<int:pk>/viajeros', ViajerosCompraView.as_view(), name='reservar_viajeros'),
    path('reservar/<int:pk>/detalles', DetallesCompraView.as_view(), name='reservar_detalles'),
    path('reservar/completado', CompletadoView.as_view(), name='reservar_completado'),
    
    path('reservas/', ReservasListView.as_view(), name='reservas'),
    
  
]
