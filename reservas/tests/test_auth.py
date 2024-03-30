from django.test import TestCase, Client
from django.urls import reverse
from reservas.models.viajero import Viajero
from usuarios.models import Usuario

class AuthTest(TestCase):
    def setUp(self):
        # Configura el entorno de prueba
        self.cliente = Client()
        Usuario.objects.create_superuser(username='admin', password='admin')
        
    def test_auth_ok(self):
        # Intenta acceder a la vista sin autenticación
        respuesta = self.cliente.get(reverse('home'))
        self.assertEqual(respuesta.status_code, 200) 
        
        respuesta = self.cliente.get(reverse('lista_viajeros'))
        self.assertEqual(respuesta.status_code, 302)  # Redirección a la página de inicio de sesión

        # Inicia sesión con el usuario de prueba
        self.cliente.login(username='admin', password='admin')

        # Accede a la vista con autenticación
        respuesta = self.cliente.get(reverse('lista_viajeros'))
        self.assertEqual(respuesta.status_code, 200)  # Acceso concedido

    def test_auth_fail(self):
        # Intenta acceder a la vista sin autenticación
        respuesta = self.cliente.get(reverse('lista_viajeros'))
        self.assertEqual(respuesta.status_code, 302)  # Redirección a la página de inicio de sesión

        # Inicia sesión con el usuario de prueba
        self.cliente.login(username='admin', password='adminincorrect')

        # Accede a la vista con autenticación
        respuesta = self.cliente.get(reverse('lista_viajeros'))
        self.assertEqual(respuesta.status_code, 302)  # Acceso concedido
        