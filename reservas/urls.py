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

from reservas.views import agenciaView, home, noticiasView, pasajeView, rutaView, viajeroView, viajeView, usuarioView

urlpatterns = [
    path('', home.HomeView.as_view(), name='dashboard'),
    
    path('rutas/', rutaView.RutaListView.as_view(), name='lista_rutas'),
    path('rutas/agregar/', rutaView.RutaCreateView.as_view(), name='agregar_ruta'),
    path('rutas/<int:pk>/editar/', rutaView.RutaUpdateView.as_view(), name='editar_ruta'),
    path('rutas/<int:pk>/eliminar/', rutaView.RutaDeleteView.as_view(), name='eliminar_ruta'),

    path('viajeros/', viajeroView.ViajeroListView.as_view(), name='lista_viajeros'),
    path('viajeros/agregar/', viajeroView.ViajeroCreateView.as_view(), name='agregar_viajero'),
    path('viajeros/<int:pk>/editar/', viajeroView.ViajeroUpdateView.as_view(), name='editar_viajero'),
    path('viajeros/<int:pk>/eliminar/', viajeroView.ViajeroDeleteView.as_view(), name='eliminar_viajero'),

    path('agencias/', agenciaView.AgenciaListView.as_view(), name='lista_agencias'),
    path('agencias/agregar/', agenciaView.AgenciaCreateView.as_view(), name='agregar_agencia'),
    path('agencias/<int:pk>/editar/', agenciaView.AgenciaUpdateView.as_view(), name='editar_agencia'),
    path('agencias/<int:pk>/eliminar/', agenciaView.AgenciaDeleteView.as_view(), name='eliminar_agencia'),
    
    path('pasajes/', pasajeView.PasajeListView.as_view(), name='lista_pasajes'),
    path('pasajes/agregar/', pasajeView.PasajeCreateView.as_view(), name='agregar_pasaje'),
    path('pasajes/<int:pk>/editar/', pasajeView.PasajeUpdateView.as_view(), name='editar_pasaje'),
    path('pasajes/<int:pk>/eliminar/', pasajeView.PasajeDeleteView.as_view(), name='eliminar_pasaje'),
    
    path('viajes/', viajeView.ViajeListView.as_view(), name='lista_viajes'),
    path('viajes/agregar/', viajeView.ViajeCreateView.as_view(), name='agregar_viaje'),
    path('viajes/<int:pk>/editar/', viajeView.ViajeUpdateView.as_view(), name='editar_viaje'),
    path('viajes/<int:pk>/eliminar/', viajeView.ViajeDeleteView.as_view(), name='eliminar_viaje'),
    
    path('noticias/', noticiasView.NoticiaListView.as_view(), name='lista_noticias'),
    path('noticias/agregar/', noticiasView.NoticiaCreateView.as_view(), name='agregar_noticia'),
    path('noticias/<int:pk>/editar/', noticiasView.NoticiaUpdateView.as_view(), name='editar_noticia'),
    path('noticias/<int:pk>/eliminar/', noticiasView.NoticiaDeleteView.as_view(), name='eliminar_noticia'),
    
    path('usuarios/', usuarioView.UsuarioListView.as_view(), name='lista_usuarios'),
    # path('usuarios/agregar/', noticiasView.NoticiaCreateView.as_view(), name='agregar_noticia'),
    # path('usuarios/<int:pk>/editar/', noticiasView.NoticiaUpdateView.as_view(), name='editar_noticia'),
    path('usuarios/<int:pk>/eliminar/', usuarioView.UsuarioDeleteView.as_view(), name='eliminar_usuario'),
    
]