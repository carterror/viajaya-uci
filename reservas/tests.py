from django.test import TestCase, Client
from django.urls import reverse
from reservas.models.viajero import Viajero
from usuarios.models import Usuario

# lista_viajeros
# agregar_viajero
# editar_viajero
# eliminar_viajero
class AuthTest(TestCase):
    def setUp(self):
        # Configura el entorno de prueba
        self.cliente = Client()
        Usuario.objects.create_user(username='admin', password='admin')
        
    def test_auth_ok(self):
        # Intenta acceder a la vista sin autenticación
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
        
    
class ViajeroUnitTest(TestCase):
    def setUp(self):
        usuario = Usuario.objects.create_superuser(
            'admin', 'admin@test.com', 'admin', ci = '00110367543'
        )
        
        self.viajero = Viajero.objects.create(
            nombre = 'Carlos Brayan',
            ci = '00110367543',
            user = usuario,
        )
    
    def test_model(self):
        # Configura el objeto de prueba
        viajero = Viajero.objects.first()
        self.assertEqual(viajero.nombre, 'Carlos Brayan')
        self.assertEqual(viajero.ci, '00110367543')
        self.assertEqual(viajero.user.username, 'admin')

# Prueba de integración
class IntegracionTestCase(TestCase):
    def setUp(self):
        # Configura el entorno de prueba
        self.client = Client()
        usuario = Usuario.objects.create_user(username='admin', password='admin')

        Viajero.objects.create(
            nombre = 'Carlos Brayan',
            ci = '00110367543',
            user = usuario,
        )
        Viajero.objects.create(
            nombre = 'Javier Gonzalez',
            ci = '00110367543',
            user = usuario,
        )
        
    def test_list_ok(self):
        self.client.login(username='admin', password='admin')
        
        # Obtener la URL de la vista
        url = reverse('lista_viajeros')
        # Realizar la solicitud GET a la vista
        response = self.client.get(url)
        # Verificar que la respuesta es 200 OK
        self.assertEqual(response.status_code, 200)
        # Verificar que la plantilla correcta se esté utilizando
        self.assertTemplateUsed(response, 'viajeros/lista_viajeros.html')
        # Verificar que los usuarios estén en el contexto de la respuesta
        viajeros_en_contexto = response.context['viajeros']
        self.assertEqual(len(viajeros_en_contexto), 2)
        # Verificar que los datos de los usuarios estén en el contenido de la respuesta
        self.assertContains(response, 'Carlos Brayan')
        self.assertContains(response, 'Javier Gonzalez')